from django.contrib import messages
from django.shortcuts import render, redirect

from mainapp.forms import CustomerRegister, Loginregister, FeedBack, CardPayment
from mainapp.models import customerreg, feedback, notification, timeschedule, appointment, bill, card_payment


def customerbase(request):
    return render(request,"customer/customerbase.html")


def customerbasereg(request):
    return render(request,"customer/customerregbase.html")

def reguser(request):
    form1 = Loginregister()
    form2 = CustomerRegister()
    if request.method == "POST":
        form1 = Loginregister(request.POST)
        form2 = CustomerRegister(request.POST)
        if form1.is_valid() and form2.is_valid():
            data = form1.save(commit=False)
            data.is_customer = True
            data.save()
            data1 = form2.save(commit=False)
            data1.user = data
            data1.save()
        return redirect("login_view")
    return render(request,"customer/customerreg.html", {'form1': form1, 'form2': form2})




def customer_feedback(request,):
    form = FeedBack()
    if request.method == "POST":
        form = FeedBack(request.POST)
        if form.is_valid():
            data1 = form.save(commit=False)
            data1.customer = customerreg.objects.get(user=request.user)
            data1.save()
            messages.info(request,"feedback added succesfully")
            return redirect("customer_feedback")
    return render(request,"customer/customer_feedback.html", {'form': form})



def feedback_view(request):
    data1 = customerreg.objects.get(user=request.user)
    data2 = feedback.objects.filter(customer=data1)
    return render(request,"customer/feedback_view.html",{"data2": data2})



def notification_viewcust(request):
    data = notification.objects.all()
    return render(request,"customer/notification_viewcust.html",{'data':data})


def scheduleviewcust(request):
    data = timeschedule.objects.all()
    return render(request,"customer/schduleviewcust.html",{'data':data})



def schedulebook(request,id):
    s = timeschedule.objects.get(id=id)
    c = customerreg.objects.get(user=request.user)
    Appointment = appointment.objects.filter(customer=c, schedule=s)
    if Appointment.exists():
        messages.info(request,'you have already requested appointment for this schedule ')
        return redirect("scheduleviewcust")
    else:
        if request.method == 'POST':
            obj = appointment()
            obj.customer = c
            obj.schedule = s
            obj.save()
            messages.info(request,'appointment booked successfully')
            return redirect("scheduleviewcust")
    return render(request, "customer/schdulebook.html", {'schedule':s})


def appointment_status(request):
    a = customerreg.objects.get(user=request.user)
    b = appointment.objects.filter(customer=a)
    return render(request,"customer/appointment_status.html",{"a":b})

def payment_view(request):
    a = customerreg.objects.get(user=request.user)
    data = bill.objects.filter(name=a)
    return render(request,"customer/payment_view.html",{"data":data})

def direct_payment(request,id):
    a = bill.objects.get(id=id)
    a.status = 2
    a.save()
    messages.info(request,"choose to pay directly")
    return redirect("payment_view")

def cardpayment(request,id):
    bi = bill.objects.get(id=id)
    form = CardPayment()

    if request.method == 'POST':
        b = request.POST.get('card')
        c = request.POST.get('cvv')
        d = request.POST.get('exp.')
        card_payment(card_no=b,card_cvv=c,expiry_date=d).save
        bi.status = 1
        bi.save()
        messages.info(request,"bill paid successfully")
        return redirect("payment_view")
    return render(request, "customer/card_payment.html", {"form": form})





from django.contrib import messages
from django.shortcuts import render, redirect

from mainapp.forms import NotificationForm, WorkForm, BillPayment
from mainapp.models import work, workerreg, customerreg, timeschedule, feedback, notification, appointment, bill


def admin1(request):
    return render(request,"admin.html")


def adminbase(request):
    return render(request,"admin/adminbase.html")


def worke_add(request):
    form = WorkForm()
    if request.method == "POST":
        form = WorkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("worke_add")
    return render(request,"admin/workadd.html",{"form":form})



def work_view(request):
    data = work.objects.all()
    return render(request,"admin/workadd_view.html",{"data":data})



def delete(request,id):
    if request.method =='POST':
        work.objects.get(id=id).delete()
        return redirect("work_view")



def ViewWorker(request):
    data = workerreg.objects.all()
    return render(request,"admin/view_worker.html",{"data":data})




def deleteW(request,id):
    if request.method =='POST':
       workerreg.objects.get(id=id).delete()
       return redirect("ViewWorker")


def ViewCustomer(request):
    data = customerreg.objects.all()
    return render(request,"admin/view_customer.html",{"data":data})

def deleteC(request,id):
    if request.method =='POST':
       customerreg.objects.get(id=id).delete()
       return redirect("ViewCustomer")

def ViewWorkerschedule(request):
    data = timeschedule.objects.all()
    return render(request,"admin/view_workerschedule.html",{"data":data})


def ViewcustomerFeedback(request):
    data = feedback.objects.all()
    return render(request,"admin/view_customerfeedback.html",{"data":data})


def CustomerFeedbackReply(request,id):
    data = feedback.objects.get(id=id)
    if request.method == 'POST':
        data1 = request.POST.get('reply')
        data.reply = data1
        data.save()
        messages.info(request,"Reply send for feedback ")
        return redirect('ViewcustomerFeedback')
    return render(request,"admin/customerdeedback_reply.html",{"data":data})



def NotificationAdd(request):
    form = NotificationForm()
    if request.method == "POST":
        form = NotificationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("NotificationAdd")
    return render(request, "admin/notificationadd.html", {"form": form})


def notificationiew_admin(request,):
    data = notification.objects.all()
    return render(request,"admin/notificationview.html", {"data":data})


def deletenot(request,id):
    if request.method =='POST':
       notification.objects.get(id=id).delete()
       return redirect("notificationiew_admin")

def booking_status(request):
    data = appointment.objects.all()
    return render(request,"admin/bookin_status.html",{"data":data})

def status_approve(request,id):
    b = appointment.objects.get(id=id)
    b.status=1
    b.save()
    messages.info(request, 'status approve successfully')
    return redirect('booking_status')

def status_reject(request,id):
    c = appointment.objects.get(id=id)
    c.status=2
    c.save()
    messages.info(request, 'status rejected')
    return redirect('booking_status')


def Bill_Payments(request):
    form = BillPayment()
    if request.method == "POST":
        form = BillPayment(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Bill_Payments")
    return render(request, "admin/payment.html", {"form": form})


def payment_status(request):
    data = bill.objects.all()
    return render(request,"admin/payment_status.html",{"data":data})

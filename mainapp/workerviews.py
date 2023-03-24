from django.shortcuts import render, redirect

from mainapp.forms import WorkForm, Loginregister, WorkerRegister, TimeSchedule
from mainapp.models import workerreg, timeschedule, notification


def workerbase(request):
    return render(request, "worker/workerbase.html",)

def regworkrbase(request):
    return render(request,"worker/workregbase.html")


def regworkr(request):
    form1 = Loginregister()
    form2 = WorkerRegister()
    if request.method == "POST":
        form1 = Loginregister(request.POST)
        form2 = WorkerRegister(request.POST,request.FILES)
        if form1.is_valid() and form2.is_valid():
            data = form1.save(commit=False)
            data.is_worker = True
            data.save()
            data1 = form2.save(commit=False)
            data1.user = data
            data1.save()
            return redirect("login_view")
    return render(request, "worker/workerreg.html", {'form1': form1, 'form2': form2})


def regupdate(request,id):
    data = workerreg.objects.get(id=id)
    form = WorkerRegister(instance=data)
    if request.method == 'POST':
        form = WorkerRegister(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
        return redirect("ViewWorker")
    return render(request,"worker/workreg_update.html",{'form': form})

def ScheduleAdd(request):
    form = TimeSchedule()
    if request.method == "POST":
        form = TimeSchedule(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.worker = workerreg.objects.get(user=request.user)
            form.save()
            return redirect("ScheduleView")
    return render(request, "worker/schedule_add.html", {"form": form})


def ScheduleView(request):
    data1 = workerreg.objects.get(user=request.user)
    data2 = timeschedule.objects.filter(worker=data1)
    return render(request,"worker/schdule_view.html", {"data2": data2})


def ScheduleUpdate(request,id):
    data = timeschedule.objects.get(id=id)
    form = TimeSchedule(instance=data)
    if request.method == 'POST':
        form = TimeSchedule(request.POST, instance=data)
        if form.is_valid():
            form.save()
        return redirect("ScheduleView")
    return render(request,"worker/schduleupdate.html", {'form': form})


def deleteSchedule(request,id):
    if request.method =='POST':
       timeschedule.objects.get(id=id).delete()
       return redirect("ViewWorkerschedule")


def NotificationView(request):
    data = notification.objects.all()
    return render(request,"worker/Notification_viewWorker.html",{'data':data})
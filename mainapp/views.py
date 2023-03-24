from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


# Create your views here.
def land(request):
    return render(request,"land.html")


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect("adminbase")
            elif user.is_worker:
                return redirect("workerbase")
            elif user.is_customer:
                return redirect("customerbase")
        else:
            messages.info(request, 'invalid Credentials')
    return render(request,"login.html")



















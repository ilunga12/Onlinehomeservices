from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class work(models.Model):
    job = models.CharField(max_length=100)

    def __str__(self):
        return self.job


class Login(AbstractUser):
    is_worker = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)


class workerreg(models.Model,):
    user = models.ForeignKey(Login, on_delete=models.CASCADE, related_name="worker")
    work = models.ForeignKey(work, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.TextField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    profilepic = models.FileField(upload_to='documents/')
    def __str__(self):
        return self.name


class customerreg(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE, related_name="customer")
    name = models.CharField(max_length=100)
    address = models.TextField(max_length=100)
    mobnumber = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.name


class timeschedule(models.Model):
    worker = models.ForeignKey(workerreg, on_delete=models.CASCADE, )
    work = models.ForeignKey(work, on_delete=models.CASCADE)
    startingtime = models.TimeField(max_length=100)
    endingtime = models.TimeField(max_length=100)
    date = models.DateField(max_length=100)


class feedback(models.Model):
    customer = models.ForeignKey(customerreg, on_delete=models.CASCADE)
    message = models.CharField(max_length=100)
    reply = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(max_length=100, auto_now=True)


class notification(models.Model):
    Notification = models.CharField(max_length=100)
    Date = models.DateField(max_length=100,auto_now=True)

class appointment(models.Model):
    customer = models.ForeignKey(customerreg, on_delete=models.CASCADE)
    schedule = models.ForeignKey(timeschedule, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)

class bill(models.Model):
    name = models.ForeignKey(customerreg,on_delete=models.CASCADE)
    billDate = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    paidOn = models.DateField(auto_now=True)
    status = models.IntegerField(default=0)


class card_payment(models.Model):
    card_no = models.CharField(max_length=100)
    card_cvv = models.CharField(max_length=100)
    expiry_date = models.CharField(max_length=100)








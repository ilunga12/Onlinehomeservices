import re

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from django.forms import TimeInput, DateInput

from mainapp.models import work, Login, customerreg, timeschedule, feedback, notification, appointment, bill, \
    card_payment, workerreg


def phone_number_validator(value):
    if not re.compile(r'^[7-9]\d{9}$').match(value):
        raise ValidationError('This is Not a Valid Phone Number')



class WorkForm(forms.ModelForm):
    class Meta:
        model = work
        fields=("__all__")


class Loginregister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label="password",widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirm password",widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ("username","password1","password2")




class WorkerRegister(forms.ModelForm):
    email = forms.CharField(validators=[
        RegexValidator(regex='^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', message='Please Enter a Valid Email')])
    phone = forms.CharField(validators=[phone_number_validator])

    class Meta:
        model = workerreg
        fields = ("work", "name", "address", "phone", "email", "profilepic")




class CustomerRegister(forms.ModelForm):
    email = forms.CharField(validators=[
        RegexValidator(regex='^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', message='Please Enter a Valid Email')])
    mobnumber = forms.CharField(validators=[phone_number_validator])


    class Meta:
        model = customerreg
        fields = ("name","address","mobnumber","email")


class timeinput(forms.TimeInput):
    input_type = "time"

class dateinput(forms.DateInput):
    input_type = "date"



class TimeSchedule(forms.ModelForm):
     startingtime = forms.TimeField(widget=timeinput)
     endingtime = forms.TimeField(widget=timeinput)
     date = forms.DateField(widget=dateinput)
     class Meta:
        model = timeschedule
        fields = ("startingtime","endingtime","date","work")



class FeedBack(forms.ModelForm):
    class Meta:
        model = feedback
        fields = ("message",)


class FeedbackReply(forms.ModelForm):
    class Meta:
        model = feedback
        fields = ("__all__")


class NotificationForm(forms.ModelForm):
    class Meta:
        model = notification
        fields = ("Notification",)

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = appointment
        fields = ("status",)
#
class BillPayment(forms.ModelForm):
    class Meta:
        model = bill
        fields = ("amount","name")


class CardPayment(forms.ModelForm):
    class Meta:
        model = card_payment
        fields = ("card_no","card_cvv","expiry_date")
from django import forms
from django.contrib import admin
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from mainapp import models
from mainapp.forms import WorkerRegister
from mainapp.models import workerreg

# Register your models here.
admin.site.register(models.work),
admin.site.register(models.Login),
admin.site.register(models.workerreg),
admin.site.register(models.customerreg),
admin.site.register(models.timeschedule),
admin.site.register(models.feedback),
admin.site.register(models.notification),
admin.site.register(models.appointment),
admin.site.register(models.bill),
admin.site.register(models.card_payment),

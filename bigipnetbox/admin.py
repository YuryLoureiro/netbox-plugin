"""
from django.contrib import admin
import .models


@admin.register(models.MyModel1)
class MyModel1Admin(admin.ModelAdmin):
    fields = '__all__'
"""
from django.contrib import admin
from .models import Node

""" Admin view for Settings """


@admin.register(Node)
class BigIPNetboxAdmin(admin.ModelAdmin):
    list_display = ("name","description","state")
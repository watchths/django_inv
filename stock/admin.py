from django.contrib import admin
from django.contrib.admin.models import LogEntry
from .models import Item, Category, Division, Employee, Inventory
# Register your models here.

admin.site.register(LogEntry)
admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Division)
admin.site.register(Employee)
admin.site.register(Inventory)
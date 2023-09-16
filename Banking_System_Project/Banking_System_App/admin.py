from django.contrib import admin

# Register your models here.
from Banking_System_App.models import Customers,TransferHistory
admin.site.register(Customers)
admin.site.register(TransferHistory)
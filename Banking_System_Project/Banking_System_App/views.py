from django.shortcuts import render,HttpResponse
from .models import Customers,TransferHistory
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.utils.timezone import localtime
import datetime
# Create your views here.
def home(request):
    return render(request, 'home.html')

def all_customers(request):
    customer_details=Customers.objects.all()
    return render(request,'all_customers.html',{'customer':customer_details})    

def customer(request,id):
    cus=Customers.objects.get(cust_id=id)
    customer_all=Customers.objects.all()
    def rem_id(val):
        if(val.cust_id)!=id:
            return True
        else:
            return False    
    customer_all=list(filter(rem_id,customer_all))        
    return render(request,'customer.html',{'customer':cus,'customer_all':customer_all})     

def transfer(request,id1,id2):
    cus1=Customers.objects.get(cust_id=id1)
    cus2=Customers.objects.get(cust_id=id2)
    return render(request,'transfer.html',{'customer1':cus1,'customer2':cus2})

def tran(request,id1,id2):
    transfer_val=int(request.GET['transferval'])
    customer1=Customers.objects.get(cust_id=id1)
    customer2=Customers.objects.get(cust_id=id2)
    customer1.balance=customer1.balance-transfer_val
    customer2.balance=customer2.balance+transfer_val
    s=''
    if request.GET:
        if (customer1.balance<0 or transfer_val<0):
            s='Transfer Unsuccessful'
        else:
            customer1.save()
            customer2.save()
            TransferHistory.objects.create(sender=customer1.name,receiver=customer2.name,amount=transfer_val,date=datetime.datetime.now())
            s='Transfer Successful'
    return render(request,'transfer.html',{'result':s,'customer1':customer1,'customer2':customer2})    

def search(request):
    search_val=request.GET['search_val']
    customer_det=Customers.objects.all()
    def fun(customer_n):
        if search_val.lower() in customer_n.name.lower():
            return True
        else:
            return False
    customer_det=list(filter(fun,customer_det))
    return render(request,'all_customers.html',{'customer':customer_det})  

def history(request):
    history_details=TransferHistory.objects.all()
    return render(request,'transfer_history.html',{'history':history_details})

def about(request):
    return render(request, 'about_us.html')
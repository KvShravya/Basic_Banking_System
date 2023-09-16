from django.db import models

# Create your models here.
class Customers(models.Model):
    cust_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    phone_no=models.IntegerField()
    email=models.EmailField(max_length=100)
    DOB=models.CharField(max_length=50)
    balance=models.IntegerField()
    address=models.CharField(max_length=200)

    def _str_(self):
        return self.cust_id

class TransferHistory(models.Model):
    id=models.AutoField(primary_key=True)
    sender=models.CharField(max_length=100)
    receiver=models.CharField(max_length=100)
    amount=models.IntegerField()
    date=models.DateField()

    def _str_(self):
        return self.id
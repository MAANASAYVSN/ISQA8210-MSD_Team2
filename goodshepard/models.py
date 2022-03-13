from django.db import models
from django.db.models import CharField
from django.utils import timezone
from django.contrib.auth.models import User


# from ckeditor.fields import RichTextField


class Client(models.Model):
    fname = models.CharField(max_length=50, blank=False, null=False)
    lname = models.CharField(max_length=50, blank=False, null=False)
    DOB = models.DateField(blank=False, null=False)
    gender = models.CharField(max_length=20, blank=False, null=False)
    address = models.CharField(max_length=100, blank=False, null=False)
    city = models.CharField(max_length=50, blank=False, null=False)
    state = models.CharField(max_length=2, blank=False, null=False)
    zip = models.CharField(max_length=5, blank=False, null=False)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    username = models.CharField(max_length=50, blank=False, null=False)
    password = models.CharField(max_length=50, blank=False, null=False)
    referredby = models.CharField(max_length=1000)
    referredto = models.CharField(max_length=1000)

    def __str__(self):
        return self.username


class Volunteer(models.Model):
    fname = models.CharField(max_length=50, blank=False, null=False)
    lname = models.CharField(max_length=50, blank=False, null=False)
    DOB = models.DateField(blank=False, null=False)
    gender = models.CharField(max_length=20, blank=False, null=False)
    address = models.CharField(max_length=100, blank=False, null=False)
    city = models.CharField(max_length=50, blank=False, null=False)
    state = models.CharField(max_length=2, blank=False, null=False)
    zip = models.CharField(max_length=5, blank=False, null=False)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    username = models.CharField(max_length=50, blank=False, null=False)
    password = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.username
# We might want to add in days the volunteers are normally available


class Employee(models.Model):
    fname = models.CharField(max_length=50, blank=False, null=False)
    lname = models.CharField(max_length=50, blank=False, null=False)
    DOB = models.DateField(blank=False, null=False)
    gender = models.CharField(max_length=20, blank=False, null=False)
    address = models.CharField(max_length=100, blank=False, null=False)
    city = models.CharField(max_length=50, blank=False, null=False)
    state = models.CharField(max_length=2, blank=False, null=False)
    zip = models.CharField(max_length=5, blank=False, null=False)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    username = models.CharField(max_length=50, blank=False, null=False)
    password = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.username


class Visit(models.Model):
    visit_note = models.CharField(max_length=2000)
    date = models.DateField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.date, self.client


class Inventory(models.Model):
    UPScode = models.CharField(max_length=15)
    item_description = models.CharField(max_length=100)

    def __str__(self):
        return self.UPScode, self.item_description


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    UPScode = models.ForeignKey(Inventory, on_delete=models.CASCADE, related_name='inventory_UPScode')
    item_description = models.ForeignKey(Inventory, on_delete=models.CASCADE, related_name='inventory_item_description')
    request_quantity = models.IntegerField(blank=False, null=False)
    delivered_quantity = models.IntegerField(blank=False, null=False)
    date = models.ForeignKey(Visit, on_delete=models.CASCADE)

    def __str__(self):
        return self.client, self.date

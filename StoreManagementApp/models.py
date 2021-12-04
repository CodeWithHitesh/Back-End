import datetime
from address.models import AddressField
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.deletion import CASCADE
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
# Create your models here.


class School(models.Model):
    school_id = models.AutoField(primary_key=True)
    school_name = models.CharField(max_length=50)
    school_phone = models.IntegerField(validators=[
        MaxValueValidator(9999999999), MinValueValidator(1000000000)])
    school_email_id = models.EmailField(max_length=50)
    object = models.Manager()


# GENDER_CHOICES = (
#     ("Male", "MALE"),
#     ("Female", "FEMALE"),
#     ("Neutral", "NEUTRAL"),
# )

# SEASON_CHOICES = (
#     ("Winter", "WINTER"),
#     ("Summer", "SUMMER"),
#     ("Neutral", "NEUTRAL"),
# )

# SIZE_CHOICES = (
#     ("XS", "xs"),
#     ("S", "s"),
#     ("M", "m"),
#     ("L", "l"),
#     ("XL", "xl"),
#     ("XXL", "xxl"),
#     ("NEUTRAL", "Neutral"),
# )


def year_choices():
    year = [(1984, 1984), ]
    for r in range(1984, datetime.date.today().year):
        year.append((r, r))
    year = tuple(year)
    return year


YEAR_CHOICES = year_choices()


def current_year():
    return datetime.date.today().year


def current_date():
    return datetime.date.today()


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    pname = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    season = models.CharField(max_length=10)
    white_uniform = models.CharField(max_length=4)
    size = models.CharField(max_length=10)
    sp = models.PositiveIntegerField()
    cp = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    c_gst = models.IntegerField(validators=[
        MaxValueValidator(30), MinValueValidator(0)])
    s_gst = models.IntegerField(validators=[
        MaxValueValidator(30), MinValueValidator(0)])
    mfd = models.IntegerField(
        ('year'), choices=YEAR_CHOICES)
    school_id = models.ForeignKey(School, on_delete=models.CASCADE)
    object = models.Manager()


class Job(models.Model):
    id = models.AutoField(primary_key=True)
    job = models.CharField(max_length=20)
    object = models.Manager()


class Staff(models.Model):
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    salary = models.PositiveIntegerField(validators=[
        MaxValueValidator(200000), MinValueValidator(1000)])
    id = models.AutoField(primary_key=True)
    date_of_birth = models.DateField()
    sname = models.CharField(max_length=20)
    joining_date = models.DateField(default=datetime.datetime.now)
    address = models.CharField(max_length=100)
    object = models.Manager()


class Staff_phoneno(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    phone_no = models.IntegerField(validators=[
        MaxValueValidator(9999999999), MinValueValidator(1000000000)])
    object = models.Manager()

    class Meta:
        unique_together = (('staff_id', 'phone_no'),)


class Customer(models.Model):
    cname = models.CharField(max_length=50)
    age = models.IntegerField(validators=[
        MaxValueValidator(150), MinValueValidator(1)])
    address = models.CharField(max_length=100)
    customer_id = models.AutoField(primary_key=True)
    object = models.Manager()


class customer_phoneno(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    phone_no = models.IntegerField(validators=[
        MaxValueValidator(9999999999), MinValueValidator(1000000000)])
    object = models.Manager()


class Registered_Customer(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    discount = models.DecimalField(max_digits=4, decimal_places=2)
    object = models.Manager()


class Buy(models.Model):
    Customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    object = models.Manager()


class Scred(models.Model):
    sname = models.CharField(max_length=20)
    spass = models.CharField(max_length=20)
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    object = models.Manager()


class Bill(models.Model):
    invoice_no = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)
    object = models.Manager()


class BillDetails(models.Model):
    id = models.AutoField(primary_key=True)
    invoice_no = models.ForeignKey(Bill, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField()
    objects = models.Manager()

from StoreManagementApp.models import Bill, Customer, Job, Product, Buy, Registered_Customer, School, Scred, Staff, Staff_phoneno, customer_phoneno
from django.contrib import admin

# Register your models here.
admin.site.register(Product)
admin.site.register(customer_phoneno)
admin.site.register(Staff_phoneno)
admin.site.register(Staff)
admin.site.register(Job)
admin.site.register(Bill)
admin.site.register(Registered_Customer)
admin.site.register(Customer)
admin.site.register(Buy)
admin.site.register(Scred)
admin.site.register(School)

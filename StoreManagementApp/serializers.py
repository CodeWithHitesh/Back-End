from django.db.models.base import Model
from rest_framework import response, serializers

from StoreManagementApp.models import Bill, BillDetails, Customer, Job, Product, Registered_Customer, School, Scred, Staff, Staff_phoneno, customer_phoneno
from StoreManagementApp.models import Buy


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class JobSerializers(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"


class SchoolSerializers(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = "__all__"


class StaffSerializers(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['Job'] = JobSerializers(instance.job_id).data
        return response


class ScredSerializers(serializers.ModelSerializer):
    class Meta:
        model = Scred
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['Staff'] = StaffSerializers(instance.staff_id).data
        return response


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['Customer'] = CustomerSerializers(
            instance.customer_id).data
        return response


class BillDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillDetails
        fields = "__all__"


class Staff_phonenoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Staff_phoneno
        fields = "__all__"

    # def to_representation(self, instance):
    #     response = super().to_representation(instance)
    #     response['Staff'] = StaffSerializers(instance.staff_id).data
    #     return response


class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class Customer_phonenoSerializers(serializers.ModelSerializer):
    class Meta:
        model = customer_phoneno
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['Customer'] = CustomerSerializers(instance.customer_id).data
        return response


class Registered_CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Registered_Customer
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['Customer'] = CustomerSerializers(instance.customer_id).data
        return response


class BuySerializers(serializers.ModelSerializer):
    class Meta:
        model = Buy
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['Customer'] = StaffSerializers(instance.customer_id).data
        return response

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['Product'] = ProductSerializers(instance.product_id).data
        return response

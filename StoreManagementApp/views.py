from datetime import datetime, timedelta
from django.http import Http404

from django.db.models import Sum
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication

from StoreManagementApp import serializers
from StoreManagementApp.models import Bill, BillDetails, Customer, Job, Product, Registered_Customer, School, Scred, Staff, Staff_phoneno, customer_phoneno, Buy
from StoreManagementApp.serializers import BillSerializer, BuySerializers, CustomerSerializers, Customer_phonenoSerializers, JobSerializers, ProductSerializers, Registered_CustomerSerializers, ScredSerializers, StaffSerializers, Staff_phonenoSerializers, SchoolSerializers


class Staff_phonenoViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        try:
            serializer = Staff_phonenoSerializers(
                data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False,
                             "message": "Staff Phone No. Data Save Successfully"}
        except:
            dict_response = {
                "error": True,
                "message": "Error During Saving Staff Phone No. Data"}
        return Response(dict_response)


class SchoolViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        school = School.object
        serializer = SchoolSerializers(
            school, many=True, context={"request": request})
        response_dict = {
            "error": False, "message": "All School List Data", "data": serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:
            serializer = SchoolSerializers(
                data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False,
                             "message": "School Data Save Successfully"}
        except:
            dict_response = {"error": True,
                             "message": "Error During Saving School Data"}
        return Response(dict_response)

    def retrieve(self, request, pk=None):
        queryset = School.object
        school = get_object_or_404(queryset, pk=pk)
        serializer = SchoolSerializers(school, context={"request": request})

        serializer_data = serializer.data

        return Response({"error": False, "message": "Single Data Fetch", "data": serializer_data})

    def update(self, request, pk=None):
        try:
            queryset = School.object
            school = get_object_or_404(queryset, pk=pk)
            serializer = SchoolSerializers(
                school, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False,
                             "message": "Successfully Updated School Data"}
        except:
            dict_response = {"error": True,
                             "message": "Error During Updating School Data"}

        return Response(dict_response)

    def destroy(self, request, pk=None):
        queryset = School.object
        school = get_object_or_404(queryset, pk=pk)
        school.delete()
        dict_response = {"error": False,
                         "message": "Successfully Deleted School Data"}
        return Response(dict_response)


class ProductViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        # if request.data.data.sp < request.data.data.cp:
        #     return Response({"error": False,
        #                      "message": "Selling Price is greater than Cost Price"})
        try:
            serializer = ProductSerializers(
                data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False,
                             "message": "product Data Save Successfully"}
        except:
            dict_response = {"error": True,
                             "message": "Error During Saving product Data"}
        return Response(dict_response)

    def list(self, request):
        product = Product.object
        serializer = ProductSerializers(
            product, many=True, context={"request": request})
        response_dict = {
            "error": False, "message": "All Product List Data", "data": serializer.data}
        return Response(response_dict)

    def retrieve(self, request, pk=None):
        querySet = Product.object
        product = get_object_or_404(querySet, pk=pk)
        serializer = ProductSerializers(product, context={"request": request})
        return Response({"error": False, "message": "single data Fetch", "data": serializer.data})

    def update(self, request, pk=None):
        try:
            queryset = Product.object
            product = get_object_or_404(queryset, pk=pk)
            serializer = ProductSerializers(
                product, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False,
                             "message": "Product Data Updated Successfully"}
        except:
            dict_response = {"error": True,
                             "message": "Error During Updating Product Data"}

        return Response(dict_response)

    def destroy(self, request, pk=None):
        queryset = Product.object
        product = get_object_or_404(queryset, pk=pk)
        product.delete()
        dict_response = {"error": False,
                         "message": "Successfully Deleted product Data"}
        return Response(dict_response)


class SchoolOnlyViewSet(generics.ListAPIView):
    serializer_class = SchoolSerializers

    def get_queryset(self):
        return School.object


class JobOnlyViewSet(generics.ListAPIView):
    serializer_class = JobSerializers

    def get_queryset(self):
        return Job.object

# Staff Viewset


class StaffViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        try:
            serializer = StaffSerializers(
                data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False,
                             "message": "Staff Data Save Successfully"}
        except:
            dict_response = {"error": True,
                             "message": "Error During Saving Staff Data"}
        return Response(dict_response)

    def list(self, request):
        staff = Staff.object
        serializer = StaffSerializers(
            staff, many=True, context={"request": request})
        response_dict = {
            "error": False, "message": "All Staff List Data", "data": serializer.data}
        return Response(response_dict)

    def retrieve(self, request, pk=None):
        queryset = Staff.object
        employee = get_object_or_404(queryset, pk=pk)
        serializer = StaffSerializers(employee, context={"request": request})
        return Response({"error": False, "message": "Single Data Fetch", "data": serializer.data})

    def update(self, request, pk=None):
        try:

            queryset = Staff.object
            staff = get_object_or_404(queryset, pk=pk)
            serializer = StaffSerializers(
                staff, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False,
                             "message": "Staff Data Updated Successfully"}
        except:
            dict_response = {"error": True,
                             "message": "Error During Updating Staff Data"}
        return Response(dict_response)

    def destroy(self, request, pk=None):
        queryset = Staff.object
        staff = get_object_or_404(queryset, pk=pk)
        staff.delete()
        dict_response = {"error": False,
                         "message": "Successfully Deleted staff Data"}
        return Response(dict_response)


class JobViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        try:
            serializer = JobSerializers(
                data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False,
                             "message": "Job Data Save Successfully"}
        except:
            dict_response = {"error": False,
                             "message": "Error During Saving Job Data"}
        return Response(dict_response)

    def list(self, request):
        job = Job.object
        serializer = JobSerializers(
            job, many=True, context={"request": request})
        response_dict = {"error": False,
                         "message": "All job List Data", "data": serializer.data}
        return Response(response_dict)

    def retrieve(self, request, pk=None):
        querySet = Job.object
        job = get_object_or_404(querySet, pk=pk)
        serializer = JobSerializers(job, context={"request": request})
        return Response({"error": False, "message": "single data Fetch", "data": serializer.data})

    def update(self, request, pk=None):
        try:
            queryset = Job.object
            job = get_object_or_404(queryset, pk=pk)

            serializer = JobSerializers(
                job, many=True, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False,
                             "message": "job Data Updated Successfully"}
        except:
            dict_response = {"error": False,
                             "message": "Error During Updating job Data"}

        return Response(dict_response)


class ScredViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        try:
            serializer = ScredSerializers(
                data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False,
                             "message": "Scred Data Save Successfully"}
        except:
            dict_response = {"error": False,
                             "message": "Error During Saving Scred Data"}
        return Response(dict_response)


class ProductNameViewSet(generics.ListAPIView):
    serializer_class = ProductSerializers

    def get_queryset(self):
        name = self.kwargs["name"]
        return Product.object.filter(pname__contains=name)


class CustomerViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        try:
            serializer = CustomerSerializers(
                data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False,
                             "message": "Customer Data Save Successfully"}
        except:
            dict_response = {"error": False,
                             "message": "Error During Saving Customer Data"}
        return Response(dict_response)

    def list(self, request):
        customer = Customer.object
        serializer = CustomerSerializers(
            customer, many=True, context={"request": request})
        response_dict = {
            "error": False, "message": "All Customer List Data", "data": serializer.data}
        return Response(response_dict)

    def retrieve(self, request, pk=None):
        querySet = Customer.object
        customer = get_object_or_404(querySet, pk=pk)
        serializer = CustomerSerializers(
            customer, context={"request": request})
        return Response({"error": False, "message": "single data Fetch", "data": serializer.data})

    def update(self, request, pk=None):
        try:
            queryset = Customer.object
            customer = get_object_or_404(queryset, pk=pk)

            serializer = CustomerSerializers(
                customer, many=True, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False,
                             "message": "customer Data Updated Successfully"}
        except:
            dict_response = {"error": False,
                             "message": "Error During Updating customer Data"}

        return Response(dict_response)

    def destroy(self, request, pk=None):
        queryset = Customer.object
        customer = get_object_or_404(queryset, pk=pk)
        customer.delete()
        dict_response = {"error": False,
                         "message": "Successfully Deleted customer Data"}
        return Response(dict_response)


class Customer_phonenoViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        try:
            serializer = Customer_phonenoSerializers(
                data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {
                "error": False, "message": "Customer_phoneno Data Save Successfully"}
        except:
            dict_response = {
                "error": False, "message": "Error During Saving Customer_Phoneno Data"}
        return Response(dict_response)


class Registered_customerViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        try:
            serializer = Registered_CustomerSerializers(
                data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {
                "error": False, "message": "Registered customer Data Save Successfully"}
        except:
            dict_response = {
                "error": False, "message": "Error During Saving Registered customer Data"}
        return Response(dict_response)


class BuyViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        try:
            serializer = BuySerializers(
                data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False,
                             "message": "Buy Data Save Successfully"}
        except:
            dict_response = {"error": False,
                             "message": "Error During Saving Buy Data"}
        return Response(dict_response)


class GenerateBillViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        # try:
        # First #Save Customer Data
        serializer = CustomerSerializers(
            data=request.data, context={"request": request})
        serializer.is_valid()
        serializer.save()

        customer_id = serializer.data['customer_id']

        # Save Bill Data
        billdata = {}
        billdata["customer_id"] = customer_id

        serializer2 = BillSerializer(
            data=billdata, context={"request": request})
        serializer2.is_valid()
        serializer2.save()
        invoice_no = serializer2.data['invoice_no']

        # Adding and Saving Id into Product Details Table
        product_details_list = []
        for product_detail in request.data["product_details"]:
            print(product_detail)
            product_detail1 = {}
            product_detail1["id"] = product_detail["id"]
            product_detail1["invoice_no"] = invoice_no
            product_detail1["quantity"] = product_detail["quantity"]

            product_deduct = Product.object.get(id=product_detail["id"])
            product_deduct.in_stock_total = int(
                product_deduct.in_stock_total)-int(product_detail['quantity'])
            product_deduct.save()

            product_details_list.append(product_detail1)
            # print(product_detail)

        serializer3 = BillSerializer(data=product_details_list, many=True,
                                     context={"request": request})
        serializer3.is_valid()
        serializer3.save()

        dict_response = {"error": False,
                         "message": "Bill Generate Successfully"}
        # except:
        #dict_response = {"error": True, "message": "Error During Generating BIll"}
        return Response(dict_response)


class HomeApiViewset(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        customer_request = Customer.object
        customer_request_serializer = CustomerSerializers(
            customer_request, many=True, context={"request": request})

        bill_count = Bill.object
        bill_count_serializer = BillSerializer(
            bill_count, many=True, context={"request": request})

        product_count = Product.object
        product_count_serializer = ProductSerializers(
            product_count, many=True, context={"request": request})

        staff_count = Staff.object
        staff_count_serializer = StaffSerializers(
            staff_count, many=True, context={"request": request})

        bill_details = Bill.object
        profit_amt = 0
        sell_amt = 0
        buy_amt = 0
        for bill in bill_details:
            buy_amt = float(buy_amt+float(bill.product_id.sp))*int(bill.qty)
            sell_amt = float(sell_amt+float(bill.product_id.cp))*int(bill.qty)

        profit_amt = sell_amt-buy_amt

        customer_request_pending = Customer.objects.filter(status=False)
        customer_request_pending_serializer = CustomerSerializers(
            customer_request_pending, many=True, context={"request": request})

        customer_request_completed = Customer.objects.filter(status=True)
        customer_request_completed_serializer = CustomerSerializers(
            customer_request_completed, many=True, context={"request": request})

        current_date = datetime.today().strftime("%Y-%m-%d")
        current_date1 = datetime.today()
        current_date_7days = current_date1+timedelta(days=7)
        current_date_7days = current_date_7days.strftime("%Y-%m-%d")
        bill_details_today = Bill.objects.filter(added_on__date=current_date)
        profit_amt_today = 0
        sell_amt_today = 0
        buy_amt_today = 0
        for bill in bill_details_today:
            buy_amt_today = float(
                buy_amt_today+float(bill.product_id.sp))*int(bill.qty)
            sell_amt_today = float(
                sell_amt_today+float(bill.product_id.cp))*int(bill.qty)

        profit_amt_today = sell_amt_today-buy_amt_today

        bill_dates = Bill.objects.order_by().values("added_on__date").distinct()
        profit_chart_list = []
        sell_chart_list = []
        buy_chart_list = []
        for billdate in bill_dates:
            access_date = billdate["added_on__date"]

            bill_data = Bill.objects.filter(added_on__date=access_date)
            profit_amt_inner = 0
            sell_amt_inner = 0
            buy_amt_inner = 0

            for billsingle in bill_data:
                buy_amt_inner = float(
                    buy_amt_inner + float(billsingle.product_id.buy_price)) * int(billsingle.qty)
                sell_amt_inner = float(
                    sell_amt_inner + float(billsingle.product_id.sell_price)) * int(billsingle.qty)

            profit_amt_inner = sell_amt_inner - buy_amt_inner

            profit_chart_list.append(
                {"date": access_date, "amt": profit_amt_inner})
            sell_chart_list.append(
                {"date": access_date, "amt": sell_amt_inner})
            buy_chart_list.append({"date": access_date, "amt": buy_amt_inner})

        dict_respone = {"error": False, "message": "Home Page Data", "customer_request": len(customer_request_serializer.data), "bill_count": len(bill_count_serializer.data), "product_count": len(product_count_serializer.data), "staff_count": len(staff_count_serializer.data), "sell_total": sell_amt, "buy_total": buy_amt, "profit_total": profit_amt, "request_pending": len(
            customer_request_pending_serializer.data), "request_completed": len(customer_request_completed_serializer.data), "profit_amt_today": profit_amt_today, "sell_amt_today": sell_amt_today, "sell_chart": sell_chart_list, "buy_chart": buy_chart_list, "profit_chart": profit_chart_list}
        return Response(dict_respone)


product_list = ProductViewSet.as_view({"get": "list"})
product_create = ProductViewSet.as_view({"post": "create"})
product_update = ProductViewSet.as_view({"put": "update"})

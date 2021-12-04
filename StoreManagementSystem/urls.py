from django.contrib import admin
from django.db import router
from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from StoreManagementApp import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.SimpleRouter()
router.register("product", views.ProductViewSet, basename="product")
router.register("staff", views.StaffViewSet, basename="staff")
router.register("Job", views.JobViewSet, basename="Job")
router.register("Scred", views.ScredViewSet, basename="Scred")
router.register("staff_phoneno", views.Staff_phonenoViewSet,
                basename="staff_phoneno")
router.register("Customer", views.CustomerViewSet, basename="Customer")
router.register("Customer_phoneno", views.Customer_phonenoViewSet,
                basename="Customer_phoneno")
router.register("Registered_customer",
                views.Registered_customerViewSet, basename="Registered_customer")
router.register("Buy", views.BuyViewSet, basename="Buy")
router.register("school", views.SchoolViewSet, basename="school")
router.register("generate_bill_api", views.GenerateBillViewSet,
                basename="generate_bill_api")
router.register("home_api", views.HomeApiViewset, basename="home_api")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/gettoken/', TokenObtainPairView.as_view(), name="gettoken"),
    path('api/refresh_token/', TokenRefreshView.as_view(), name="refresh_token"),
    path('api/productbyname/<str:name>', views.ProductNameViewSet.as_view(),
         name="productbyname"),
    path('api/schoolonly/', views.SchoolOnlyViewSet.as_view(), name="schoolonly"),
    path('api/jobonly/', views.JobOnlyViewSet.as_view(), name="jobonly"),
]

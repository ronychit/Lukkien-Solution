from django.contrib import admin
from django.urls import path
from customer.views import CustomerCreateView,ShippingCreateView
from apiservices.views import CustomerViewSet,ShippingViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api/customer', CustomerViewSet, base_name='customer')
router.register(r'api/shipping', ShippingViewSet, base_name='shipping')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customer/create', CustomerCreateView.as_view(),name='customer_create'),
    path('shipping/create', ShippingCreateView.as_view(),name='shipping_create'),
]
urlpatterns += router.urls

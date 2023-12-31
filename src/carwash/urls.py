"""
URL configuration for carwash project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from  carwashmanagement.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home,name='home'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register', register_user, name='register'),
    path('customer_list', customer_list, name='customer-list'),
    path('record/<int:pk>', customer_record, name='record'),
    path('detelete_record/<int:pk>', delete_record, name='delete-record'),
    path('add_customer', add_Customer, name='add-customer'),
    path('update_record/<int:pk>', update_record, name='update-record'),
    path('book_services', book_services, name='book-services'),
    path('booking_table', booking_table, name='booking-table'),
    path('book-service/<int:customer_id>/', book_service_customer, name='book-services-for-customer'),
]

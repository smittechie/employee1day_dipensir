from django.contrib import admin
from django.urls import path , include

from .views import Home, AddEmployeeDetailView

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('add_employee_detail', AddEmployeeDetailView.as_view(), name='add_employee_detail'),

]

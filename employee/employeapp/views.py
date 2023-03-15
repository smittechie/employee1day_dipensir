from django.shortcuts import render
from django.views.generic import TemplateView, CreateView

from .forms import AddEmployeForm
from .models import Employee


# Create your views here.
class Home(TemplateView):
    template_name = 'employeapp/home.html'

class AddEmployeeDetailView(CreateView):
    model = Employee
    # fields = "__all__"
    form_class = AddEmployeForm
    success_url = "/"

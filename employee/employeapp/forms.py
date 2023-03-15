from django import forms

from .models import Employee


class AddEmployeForm(forms.ModelForm):
    manager = forms.ModelChoiceField(
        queryset = Employee.objects.filter(title = 'manager'),
        initial = 0
        )
    class Meta:
        model = Employee
        fields =['name','title','manager','skill','rating']

from django.forms import formset_factory
ArticleFormSet = formset_factory(AddEmployeForm,extra=2)
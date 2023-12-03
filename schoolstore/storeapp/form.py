from django import forms

from .models import Department, Course

class MyForm(forms.Form):
    department = forms.ModelChoiceField(queryset=Department.objects.all(), empty_label="Select Department")
    courses = forms.ModelChoiceField(queryset=Course.objects.none(), empty_label="Select Department First")
    # Add other form fields as needed

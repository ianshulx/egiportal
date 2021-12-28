from django import forms
from django.forms import fields
from .models import project

class projectform(forms.ModelForm):
        class Meta:
            model=project
            fields=("Project_name", "Github_link", "Project_image")
from dataclasses import fields
from .models import Client,Project_Num
from django.forms import ModelForm

class formForm(ModelForm):
    class Meta:
        model = Client
        fields = ['']
    
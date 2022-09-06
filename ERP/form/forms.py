from .models import Project_Num,Client
from django import forms

class saveForm(forms.Form):
    id_dep_client = forms.ModelChoiceField(empty_label=None, queryset=Client.objects.all(), label='Клиент №:')
    id_project = forms.ModelChoiceField(empty_label=None, queryset=Project_Num.objects.all(), label='Проект №:')
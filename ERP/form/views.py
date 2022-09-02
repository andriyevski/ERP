from urllib import response
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render
from .models import Client

# Create your views here.
def index(request):
    name = "ERP 'ba3a'"
    client_num = 'Клиент №:'
    project_name = 'Проект №:'

    response = render_to_string('form/index.html')
    return render(request,'form/index.html',{'client_num':client_num,
    'project_name':project_name, 'name':name})
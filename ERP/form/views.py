from pyexpat import model
import re
from urllib import response
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render
from .models import Client,Project_Num

# Create your views here.
def index(request):
    name = "ERP 'ba3a'"
    client_num = 'Клиент №:'
    project_name = 'Проект №:'
    client = Client.objects.all
    project_id = Project_Num.objects.all

    return render(request,'form/index.html',{'client_num':client_num,
    'project_name':project_name, 'name':name, 'client':client,'project_id':project_id})

def create(request):
    return render(request, 'form/index.html')
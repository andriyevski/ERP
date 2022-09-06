from http import client
from pyexpat import model
import re
from urllib import response
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render
from .models import Client,Project_Num
from .forms import saveForm


# Create your views here.
def index(request):
    
    if request.method == 'POST':
        form = saveForm(request.POST)
        print('Message: Post method!')
        print('Message: invalid Form!')
        print(form.data)
        if form.is_valid():
            print('Message: Form is a valid !')
            print(form.cleaned_data)
            return HttpResponse("YEAH works! Save!")
    else:
        form = saveForm()
    return render(request, 'form/index.html', {'form':form})
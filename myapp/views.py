from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Universitate

def universitet_list(request):
    universitets = Universitate.objects.all()
    print(universitets)
    universitet_list = ""
    for universitet in universitets:
        universitet_list+=f"<li>{universitet.name}</li>"
    return HttpResponse(f"<ul> {universitet_list}</ul>")
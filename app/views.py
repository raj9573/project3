from django.shortcuts import render

# Create your views here.

from app.models import *


def showstudents(request):


    so = Students.objects.all()


    return render(request,'show.html',{'so':so})

    

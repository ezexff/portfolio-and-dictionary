from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect

from django.urls import reverse

from .models import Project

# Import mimetypes module
import mimetypes
# import os module
import os

# Вызываемые методы при переходе на страницу

def index(request):
    #semesters = ['1 семестр', '2 семестр', '3 семестр', '4 семестр', '5 семестр', '6 семестр', '7 семестр', '8 семестр']
    #all_projects = Project.objects.order_by('project_title')
    #return render(request, 'portfolio/portfolio.html', {'all_projects' : all_projects, 'semesters' : semesters})
    return render(request, 'portfolio/portfolio.html')
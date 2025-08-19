from django.contrib import admin

from .models import Project

# Описание таблиц, отображаемых в панели администратора

admin.site.register(Project)
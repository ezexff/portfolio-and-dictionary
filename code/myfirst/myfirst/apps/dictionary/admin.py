from django.contrib import admin

from .models import Dictionary, Comment, Card

# Описание таблиц, отображаемых в панели администратора

admin.site.register(Dictionary)
admin.site.register(Comment)
admin.site.register(Card)
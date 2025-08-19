from django.urls import path

from . import views

app_name = 'dictionary'
urlpatterns = [
    path('', views.cards, name = 'cards'),
    #path('add_card', views.add_card, name='add_card'),
    path('<int:dictionary_id>/', views.detail, name = 'detail'),
    path('<int:dictionary_id>/leave_comment/', views.leave_comment, name = 'leave_comment'),
]
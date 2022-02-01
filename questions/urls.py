from django.urls import path
from . import views

urlpatterns= [
    path('', views.question, name='home'),
    path('<str:level>/', views.question_level, name='level'),
]
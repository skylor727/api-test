from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getjoke/', views.get_joke, name='get_joke'),
]
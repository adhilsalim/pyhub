from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='project-index'),
    path('about/', views.about, name='project-about'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
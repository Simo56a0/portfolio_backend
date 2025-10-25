from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),

    path('contact/', views.contact, name='contact'),
    path('generic/', views.generic, name='generic'),
    path('services/', views.services, name='services'),
    path('single/', views.single, name='single'),
    path('styles/', views.styles, name='styles'),
    
]

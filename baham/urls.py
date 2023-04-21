from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
     path('baham/about-us',views.about,name='aboutus'),
]
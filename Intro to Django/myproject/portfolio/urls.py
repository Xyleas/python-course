from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = 'portfolio'),
    path('about/', views.about, name = 'about')
]

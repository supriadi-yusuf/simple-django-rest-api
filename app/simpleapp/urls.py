from django.urls import path
from . import views

app_name = 'simpleapp'

urlpatterns = [
    path('calculate', views.SimpleAppView.as_view(), name='calculate')
]
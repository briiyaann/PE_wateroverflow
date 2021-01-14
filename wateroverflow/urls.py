  
from django.urls import path
from wateroverflow import views

app_name = 'wateroverflow'

urlpatterns = [
    path('', views.overflow, name='overflow')
]
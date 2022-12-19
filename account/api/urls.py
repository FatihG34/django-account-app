from django.urls import path
from .views import home

urlpatterns = [
    path("account/", home, name='home'),
    
]

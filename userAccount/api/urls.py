from django.urls import path, include
from .views import RegisterView

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("auth/", include('django.contrib.auth.urls')),
    path('rest_auth/', include('dj_rest_auth.urls')),
]

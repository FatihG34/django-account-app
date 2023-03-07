from django.urls import path, include
from .views import RegisterView, UpdateUserView, AllUsersView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'all-user', AllUsersView, basename='all-user')

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("update-profile/<str:username>", UpdateUserView.as_view()),
    path("", include(router.urls)),
    path("auth/", include('django.contrib.auth.urls')),
    path('rest_auth/', include('dj_rest_auth.urls')),
]

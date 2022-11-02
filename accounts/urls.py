from django.urls import path

from accounts.views import (
    SignupAPIView,
    SigninAPIView,
    ProfileAPIView,
)

urlpatterns = [
    path('signup/', SignupAPIView.as_view()),
    path('signin/', SigninAPIView.as_view()),
    path('profile/', ProfileAPIView.as_view()),
]

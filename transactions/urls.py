from django.urls import path

from transactions.views import ProcessFileAPIView

urlpatterns = [
    path('process-file/', ProcessFileAPIView.as_view()),
]

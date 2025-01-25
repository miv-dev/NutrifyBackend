from django.urls import path

from accounts import views

urlpatterns = [
    path('current/', views.UpdateCurrentUserView.as_view(), name='update-current-user')
]

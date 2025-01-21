from django.urls import path

from accounts import views

urlpatterns = [
    path('current/', views.RetrieveCurrentUserView.as_view(), name='current-user')
]

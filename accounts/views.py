from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response

from .serializers import UserSerializer

from accounts.models import CustomUser



class RetrieveCurrentUserView(RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        user = queryset.get(pk = request.user.pk)

        serializer = self.get_serializer(user)
        return Response(serializer.data)
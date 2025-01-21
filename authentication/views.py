from rest_framework import permissions, status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import UserRegistrationSerializer

from accounts.models import CustomUser


class CreateUserView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

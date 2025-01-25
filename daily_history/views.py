from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from daily_history.models import DailyHistory
from daily_history.serializers import DailyHistorySerializer


class DailyHistoryViewSet(viewsets.ModelViewSet):
    serializer_class = DailyHistorySerializer
    queryset = DailyHistory.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)



    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
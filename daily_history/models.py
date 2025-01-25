from django.db import models

from accounts.models import CustomUser


class DailyHistory(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="daily_histories")
    date = models.DateField(auto_now_add=True)
    total_calories = models.FloatField(default=0)
    protein = models.FloatField(default=0)
    fat = models.FloatField(default=0)
    carbs = models.FloatField(default=0)
    weight = models.FloatField(default=0)
    recipe_data = models.JSONField(default=list, blank=True)


    def __str__(self):
        return f"History for {self.user.username} on {self.date}"
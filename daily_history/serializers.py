from rest_framework import serializers

from daily_history.models import DailyHistory


class RecipeDataSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    calories = serializers.FloatField()
    protein = serializers.FloatField()
    fat = serializers.FloatField()
    carbs = serializers.FloatField()
    meal_type = serializers.CharField(max_length=32)


class DailyHistorySerializer(serializers.ModelSerializer):
    """
Serializer for the DailyHistory model, including recipe data snapshots.
    """
    recipe_data = RecipeDataSerializer(many=True)  # Serialize the list of recipe snapshots

    class Meta:
        model = DailyHistory
        fields = [
            'id',
            'date',
            'total_calories',
            'protein',
            'weight',
            'fat',
            'carbs',
            'recipe_data'
        ]
        read_only_fields = ['id', 'user', 'date']

    def create(self, validated_data):
        recipe_data = validated_data.pop('recipe_data', [])
        daily_history = DailyHistory.objects.create(**validated_data)
        daily_history.recipe_data = recipe_data
        daily_history.save()
        return daily_history

    def update(self, instance, validated_data):
        instance.total_calories = validated_data.get('total_calories', instance.total_calories)
        instance.protein = validated_data.get('protein', instance.protein)
        instance.fat = validated_data.get('fat', instance.fat)
        instance.carbs = validated_data.get('carbs', instance.carbs)
        instance.weight = validated_data.get('weight', instance.weight)

        if 'recipe_data' in validated_data:
            instance.recipe_data = validated_data['recipe_data']

        instance.save()
        return instance
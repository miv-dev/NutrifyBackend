from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import CustomUser


# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {
            'fields': (
                'age', 'gender', 'height_cm', 'weight_kg',
                'daily_calorie_goal', 'protein_goal', 'fat_goal', 'carb_goal',
                'activity_level', 'dietary_preference', 'allergies',
                'profile_picture'
            )
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            'fields': (
                'age', 'gender', 'height_cm', 'weight_kg',
                'daily_calorie_goal', 'protein_goal', 'fat_goal', 'carb_goal',
                'activity_level', 'dietary_preference', 'allergies',
                'profile_picture'
            )
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)

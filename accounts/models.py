from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(username, email, password, **extra_fields)


# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')], blank=True)
    height_cm = models.PositiveIntegerField(null=True, blank=True)  # Height in cm
    weight_kg = models.FloatField(null=True, blank=True)  # Weight in kg

    # Nutrition Goals
    daily_calorie_goal = models.PositiveIntegerField(null=True, blank=True)  # Calories (kcal)
    protein_goal = models.FloatField(null=True, blank=True)  # Protein (grams)
    fat_goal = models.FloatField(null=True, blank=True)  # Fat (grams)
    carb_goal = models.FloatField(null=True, blank=True)  # Carbs (grams)

    # Activity and Lifestyle
    activity_level = models.CharField(
        max_length=20,
        choices=[
            ('sedentary', 'Sedentary (little or no exercise)'),
            ('light', 'Lightly active (light exercise/sports 1-3 days/week)'),
            ('moderate', 'Moderately active (moderate exercise/sports 3-5 days/week)'),
            ('active', 'Active (intense exercise/sports 6-7 days a week)'),
            ('very_active', 'Very active (very intense exercise daily or physical job)')
        ],
        default='sedentary'
    )

    # Dietary Preferences
    dietary_preference = models.CharField(
        max_length=20,
        choices=[
            ('none', 'None'),
            ('vegetarian', 'Vegetarian'),
            ('vegan', 'Vegan'),
            ('keto', 'Keto'),
            ('paleo', 'Paleo'),
            ('other', 'Other')
        ],
        default='none'
    )
    allergies = models.TextField(blank=True, null=True)  # List of allergies (comma-separated)

    # Additional Fields
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    # Custom Manager
    objects = CustomUserManager()

    def __str__(self):
        return self.username
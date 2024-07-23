from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from managers import UserManager


class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Администратор'),
        ('coach', 'Тренер'),
        ('visitor', 'Посетитель'),
    ]
    GENDER_CHOICES = [
        ('male', 'Парень'),
        ('female', 'Девушка')
    ]

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=30, choices=GENDER_CHOICES, null=True, blank=True)
    height = models.PositiveIntegerField(null=True, blank=True)  # рост в сантиметрах
    weight = models.PositiveIntegerField(null=True, blank=True)  # вес в килограммах
    is_active = models.BooleanField(default=False)
    role = models.CharField(
        max_length=50,
        choices=ROLE_CHOICES,
        default='visitor'
    )
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.email

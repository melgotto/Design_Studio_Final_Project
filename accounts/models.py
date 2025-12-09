from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('designer', 'Дизайнер'),
        ('art_director', 'Арт Директор'),
        ('manager', 'Менеджер'),
        ('client', 'Клієнт'),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        name='role',
        default='client'
    )

    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.username} ({self.role})"

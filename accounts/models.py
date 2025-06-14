from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('user', 'User'),
        ('mitra', 'Mitra'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    no_hp = models.CharField(max_length=20, blank=True)
    alamat = models.TextField(blank=True)

    def __str__(self):
        return f"{self.username} ({self.role})"

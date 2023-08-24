from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


# Create your models here.

class User(AbstractUser):
    DELETED = 0
    DISABLED = 1
    INACTIVE = 2
    DEFAULT = 3
    ACTIVE = 4
    STATUS_CHOICES = (
        (DELETED, 'User deleted'),
        (DISABLED, 'User disabled'),
        (INACTIVE, 'User inactive'),
        (DEFAULT, 'Default status'),
        (ACTIVE, 'User Active')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    email = models.EmailField(unique=True)

    phone_number = models.CharField(max_length=12)

    full_name = models.CharField(max_length=200)
    username = models.CharField(max_length=255, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    last_password_change = models.DateTimeField(null=True)
    roles = ArrayField(models.IntegerField(), null=True, default=list)
    status = models.PositiveIntegerField(choices=STATUS_CHOICES, default=DEFAULT)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['full_name', 'phone_number', 'username']

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'User'


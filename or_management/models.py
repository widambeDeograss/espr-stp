from django.db import models
from user_management.models import *
from product_management.models import *
import uuid


# Create your models here.

class Order(models.Model):
    DISABLED = 0
    DEFAULT = 1
    ACTIVE = 2
    COMPLETED = 3
    STATUS_CHOICES = (
        (DISABLED, 'Order disabled'),  # order is disabled when client not interested again
        (DEFAULT, 'Default status'),  # order is initialized
        (ACTIVE, 'Order Active'),  # order is confirmed for agent to take action
        (COMPLETED, 'Order completed'),  # order is complete and client already get the product
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    initializer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='initializer')  # initialize
    agent = models.ForeignKey(User, on_delete=models.CASCADE, related_name='agent')  # agent
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    buying_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    profit = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    status = models.PositiveIntegerField(choices=STATUS_CHOICES, default=DEFAULT)

    def __str__(self):
        return f''

    class Meta:
        db_table = 'Order'


class IncomeTransaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    profit = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f''

    class Meta:
        db_table = 'Income_transaction'


class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    username = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return f''

    class Meta:
        db_table = 'Client'



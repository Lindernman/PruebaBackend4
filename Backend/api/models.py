from django.db import models
from django.db.models.functions import Now
# Create your models here.


class Users(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    money_amount = models.BigIntegerField(default=0)


class Transaction(models.Model):
    id = models.BigAutoField
    user = models.ForeignKey(
        Users, related_name='transactions', on_delete=models.CASCADE)
    amount = models.BigIntegerField(default=0)
    created_at = models.DateField(default=Now())

    class Meta:
        unique_together = ['id', 'user_id', 'amount']

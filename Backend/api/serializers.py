from rest_framework.serializers import ModelSerializer
from api.models import Users, Transaction
from rest_framework import serializers
from django.db import models


class TransactionSerializer(ModelSerializer):

    class Meta:
        model = Transaction
        fields = '__all__'


class UserSerializer(ModelSerializer):
    transactions = TransactionSerializer(many=True, required=False)

    class Meta:
        model = Users
        fields = ['user_id', 'username', 'password',
                  'money_amount', 'transactions']



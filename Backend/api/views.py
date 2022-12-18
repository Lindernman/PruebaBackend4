from rest_framework.viewsets import ModelViewSet
from api.models import Users, Transaction
from api.serializers import UserSerializer, TransactionSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class UsersApiViewSet(ModelViewSet):

    queryset = Users.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['post'])
    def login(self, request):

        queryset = Users.objects.all()
        user = get_object_or_404(queryset, username=request.POST['username'])
        serializer = UserSerializer(user)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def register(self, request):
        user = Users.objects.create(
            username=request.POST['username'],  password=request.POST['password'], money_amount=0)
        serializer = UserSerializer(instance=user)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def transaction(self, request):

        user_id = request.POST['user_id']
        Transaction.objects.create(
            user_id=user_id,  amount=request.POST['amount'])
        upuser = Users.objects.get(user_id=user_id)
        upuser.money_amount = upuser.money_amount + int(request.POST['amount'])
        upuser.save()
        queryset = Users.objects.all()
        user = get_object_or_404(queryset, user_id=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

from django.shortcuts import render
from product_management.models import *
from user_management.models import *
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated


class OrderView(APIView):
    @staticmethod
    def post(request):
        serializer = OrderPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'success', 'data': serializer.validated_data})
        return Response(serializer.errors)

    @staticmethod
    def get(request):
        queryset = Order.objects.all()
        return Response(OrderGetSerializer(instance=queryset, many=True))


class IncomeTransactionView(APIView):
    @staticmethod
    def post(request):
        serializer = IncomeTransactionPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'success'})

        return Response({'data': serializer.errors})

    @staticmethod
    def get(request):
        queryset = IncomeTransaction.objects.all()
        return Response(IncomeTransactionGetSerializer(instance=queryset, many=True).data)


class ClientView(APIView):
    @staticmethod
    def post(request):
        serializer = ClientPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'success'})
        return Response(serializer.errors)

    @staticmethod
    def get(request):
        queryset = Client.objects.all()
        return Response(ClientGetSerializer(instance=queryset, many=True).data)


class OrderStatus(APIView):
    @staticmethod
    def post(request, order_id, new_status):
        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return Response({'message': 'Order does not exist'})

        order.status = new_status
        order.save()
        return Response({'message': 'Successful change'})


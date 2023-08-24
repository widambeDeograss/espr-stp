from .models import *
from rest_framework.views import *
from .serializers import *
from rest_framework import response
from rest_framework.response import *


# Create your views here.


class BrandView(APIView):
    @staticmethod
    def post(request):
        request_data = request.data
        serializer = BrandPostSerializer(data=request_data)

        if serializer.is_valid():
            serializer.save()
            message = {'save': True}
            return Response(message)
        return Response(serializer.errors)

    @staticmethod
    def get(request):
        queryset = Brand.objects.all()
        serializable_data = BrandGetSerializer(instance=queryset, many=True).data
        return Response({"data": serializable_data})


class CategoryView(APIView):
    @staticmethod
    def post(request):
        request_data = request.data
        serializer = CategoryPostSerializer(data=request_data)

        if serializer.is_valid():
            serializer.save()
            return Response({'save': True})
        return Response(serializer.errors)

    @staticmethod
    def get(request):
        queryset = Category.objects.all()
        serializable_data = CateogoryGetSerializer(instance=queryset, many=True)
        return Response({'data': serializable_data.data})


class SubCategoryView(APIView):
    @staticmethod
    def post(request):
        data = request.data
        serializer = SubCategoryPostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            message = {'save': True}
            return Response(message)
        return Response(serializer.errors)

    @staticmethod
    def get(request):
        queryset = SubCategory.objects.values('id', 'name').all()
        # serializable_data = SubCategoryGetSerializer(instance=queryset, many=True).data
        # return Response(serializable_data.data)
        return  Response(queryset)

class ProductView(APIView):
    @staticmethod
    def post(request):
        requested_data = request.data
        print(requested_data)
        serializer = ProductPostSerializer(data=requested_data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'save': True
            })
        return Response(serializer.errors)

    @staticmethod
    def get(request):
        queryset = Product.objects.all()
        serializable_data = ProductGetSerializer(instance=queryset, many=True).data
        return Response(serializable_data)

from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from homework_8.models import Category
from homework_8.serializers.categories import CategoryCreateSerializer


class CategoryListCreateView(APIView):
    def post(self, request: Request) -> Response:
        serializer = CategoryCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailUpdateDeleteView(APIView):
    def put(self, request, category_id: int) -> Response:
        category = get_object_or_404(Category, pk=category_id)

        serializer = CategoryCreateSerializer(category, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from products.api.serializers import ProductSerializer, CategorySerializer, SubCategorySerializer
from products.models import Product, SubCategory, Category


class ProductViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'subcategory']


class SubCategoryViewset(viewsets.ReadOnlyModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class CategoryViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

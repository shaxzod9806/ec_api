from .serializers import ProductSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Product
from rest_framework import permissions
from .permissions import IsAuthorOrReadOnly


# Create your views here.
class ProductList(ListCreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (
        IsAuthorOrReadOnly,
    )
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

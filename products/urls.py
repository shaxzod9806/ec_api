from .views import ProductList, ProductDetail
from django.urls import path

urlpatterns = [
    path('<int:pk>/', ProductDetail.as_view()),
    path('', ProductList.as_view())
]

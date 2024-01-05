from django.urls import path
from products.rest_apis import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductListApiView.as_view(), name='product-list'),
    path('<str:code>/', views.ProductDetailsApiView.as_view(), name='product-details'),
]
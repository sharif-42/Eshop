from django.urls import path

from search.rest_apis import views

urlpatterns = [
     path('products/', views.ProductSearchAPIView.as_view(), name='product-search'),
]
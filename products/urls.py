from django.urls import path
from .views import ProdutList


urlpatterns = [
    path('products', ProdutList.as_view(),  name="list")
]


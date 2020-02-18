from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from inventory.views import ItemList, ItemDetail

urlpatterns = [
    path('inventory/', ItemList.as_view()),
    path('inventory/<int:pk>/', ItemDetail.as_view()),
]

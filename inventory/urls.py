from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from inventory.views import CarList, CarDetail

urlpatterns = [
    path('inventory/', CarList.as_view()),
    path('inventory/<int:pk>/', CarDetail.as_view()),
]

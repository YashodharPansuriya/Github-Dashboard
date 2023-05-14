from django.urls import path
from KPI_Dashboard.Views.GIthub_views import index

urlpatterns = [
    path('', index),
]
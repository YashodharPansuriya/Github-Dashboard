from django.urls import path
from Dashboard1.views import index

urlpatterns = [
    path('', index),
]
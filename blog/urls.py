from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', PostListCreateAPIView.as_view(), name='post-list-create'),
    path('<int:pk>', PostRetriveUpdateDestroyAPIView.as_view(), name='post-detail'),
]
from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'post', PostViewSet)

urlpatterns = [
    # path('create/', PostCreateAPIView.as_view()),
    # path('list/', PostListAPIView.as_view()),
    # path('retrieve/<int:pk>/', PostRetriveAPIView.as_view()),
    # path('update/<int:pk>/', PostUpdateAPIView.as_view()),
    # path('destroy/<int:pk>/', PostDestroyAPIView.as_view()),


    # path('', PostListCreateAPIView.as_view(), name='post-list-create'),
    # path('<int:pk>', PostRetriveUpdateDestroyAPIView.as_view(), name='post-detail'),

    path('', include(router.urls)),
]
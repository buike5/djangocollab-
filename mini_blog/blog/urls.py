from posixpath import basename
from django.urls import path

from .views import PostListView, PostViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')

urlpatterns = [
    path('', PostListView.as_view())
]
urlpatterns = [] + router.urls
path('api', PostViewSet.as_view({'get': 'list'}))

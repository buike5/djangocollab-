from django.shortcuts import render
from .models import post
from django.views.generic.list import ListView
from rest_framework import viewsets
from .serializers import PostSerializer

# Create your views here.
class PostListView(ListView):
    model = post
    template_name = "list.html"
    

class PostViewSet(viewsets.ModelViewSet):
    queryset = post.objects.all()
    serializer_class = PostSerializer




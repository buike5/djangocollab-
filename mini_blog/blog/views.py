from django.shortcuts import render
from .models import post
from django.views.generic.list import ListView

# Create your views here.
class PostListView(ListView):
    model = post
    template_name = "list.html"
    
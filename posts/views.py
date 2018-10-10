from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.
from .models import Post


class HomePageView(ListView):
    """:return objectlist"""
    model = Post
    template_name = 'posts/home.html'
from django.shortcuts import render
from django.utils import timezone
from . models import Post

# Create your views here.
def home(request):
    return render(request, 'blog/home.html', {})

def about(request):
    return render(request, 'blog/about.html', {})

def news(request):
    return render(request, 'blog/news.html', {})

def posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/posts.html', {'posts': posts})
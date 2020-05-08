from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'blog/home.html', {})

def about(request):
    return render(request, 'blog/about.html', {})

def news(request):
    return render(request, 'blog/news.html', {})

def post_list(request):
    return render(request, 'blog/post_list.html', {})
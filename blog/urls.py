from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('news', views.news, name='news'),
    path('blogposts', views.posts, name='posts'),
]
from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def posts_index(request):
  posts = Post.objects.all()

  return render(request, 'posts/index.html', {
    'posts': posts
  })
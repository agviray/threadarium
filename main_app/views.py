from django.shortcuts import render

posts = [
  {
    'title': 'Post One',
    'body': 'This is post number 1'
  },
  {
    'title': 'Post Two',
    'body': 'This is post number 2'
  },
  {
    'title': 'Post Three',
    'body': 'This is post number 3'
  },
  {
    'title': 'Post Four',
    'body': 'This is post number 4'
  },
]

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def posts_index(request):
  return render(request, 'posts/index.html', {
    'posts': posts
  })
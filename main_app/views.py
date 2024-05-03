from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from .forms import CommentForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}

  return render(request, 'registration/signup.html', context)

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def all_posts(request):
  all_posts = Post.objects.all()

  return render(request, 'posts/all_posts.html', {'all_posts': all_posts})

@login_required
def posts_index(request):
  posts = Post.objects.filter(user=request.user)

  return render(request, 'posts/index.html', {
    'posts': posts
  })

@login_required
def posts_detail(request, post_id):
  post = Post.objects.get(id=post_id)
  comment_form = CommentForm()

  return render(request, 'posts/detail.html', {
    'post': post,
    'comment_form': comment_form
  })

@login_required
def add_comment(request, post_id): 
  post = Post.objects.get(id=post_id)

  if request.method == 'POST':
    form = CommentForm(request.POST)
    if form.is_valid():
      comment = form.save(commit=False)
      comment.post_id = post_id
      comment.user_id = request.user.id
      comment.save()
      return redirect('detail', post_id=post_id)
  else: 
    form = CommentForm()

  return render(request, 'posts/detail.html', {
    'post': post,
    'form': form
  })

class PostCreate(LoginRequiredMixin, CreateView):
  model = Post
  fields = ['title', 'body']

  def form_valid(self, form):
    form.instance.user = self.request.user

    return super().form_valid(form)

class PostUpdate(LoginRequiredMixin, UpdateView):
  model = Post
  fields = ['body']

class PostDelete(LoginRequiredMixin, DeleteView):
  model = Post
  success_url = '/posts'
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # Create 'user' form objectd that includes
    # data from the browser.
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # Add user to database
      user = form.save()
      # Log user in with:
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or GET request results in rendering signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def posts_index(request):
  posts = Post.objects.all()

  return render(request, 'posts/index.html', {
    'posts': posts
  })

def posts_detail(request, post_id):
  post = Post.objects.get(id=post_id)

  return render(request, 'posts/detail.html', {'post': post})

class PostCreate(CreateView):
  model = Post
  fields = ['title', 'body']

  # This is an inherited method that will be called 
  #  when a valid post form is being submitted.
  def form_valid(self, form):
    # Assign logged in user (self.request.user)
    # Note: form.instance is the post
    form.instance.user = self.request.user

    return super().form_valid(form)

class PostUpdate(UpdateView):
  model = Post
  fields = ['body']

class PostDelete(DeleteView):
  model = Post
  success_url = '/posts'

from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('posts/all_posts/', views.all_posts, name='all_posts'),
  path('posts/', views.posts_index, name='index'),
  path('posts/<int:post_id>/', views.posts_detail, name='detail'),
  path('posts/create/', views.PostCreate.as_view(), name='post_create'),
  path('posts/<int:pk>/update/', views.PostUpdate.as_view(), name='post_update'),
  path('posts/<int:pk>/delete/', views.PostDelete.as_view(), name='post_delete'),
  path('post/<int:post_id>/comment/', views.add_comment, name='add_comment'),
  path('accounts/signup/', views.signup, name='signup'),
  path("__reload__/", include("django_browser_reload.urls")),
]
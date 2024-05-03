from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Post(models.Model):
  title = models.CharField(max_length=100)
  body = models.TextField(max_length=250)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  created_on = models.DateTimeField(auto_now_add=True)
  
  class Meta:
    ordering = ['-created_on']
  
  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={'post_id': self.id})
  
  
class Comment(models.Model):
  body = models.TextField(250)
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  created_on = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ['-created_on']
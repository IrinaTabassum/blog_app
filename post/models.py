from django.db import models
from user.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)
    descreption = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=250)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    

   
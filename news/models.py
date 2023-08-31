from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=25)
    excerpt = models.CharField(max_length=160)
    
    class Meta:
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.title

class PostModel(models.Model):
    title = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField()
    excerpt = models.CharField(max_length=160, blank=True)
    body = models.TextField()
    category = models.ManyToManyField(Category)
    
    class Meta:
        verbose_name_plural = 'posts'
        ordering = ['-created_on']
        
    def __str__(self):
        return self.title

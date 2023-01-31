from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify
import datetime

User = get_user_model()

# Create your models here.
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username
    

class Category(models.Model):
    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=20)
    slug = models.SlugField(allow_unicode=True, unique=True, max_length=250, null=True, blank=True)
    thumbnail = models.ImageField()

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):  # new
        if not self.slug:
            slug_str = f"{self.title}-{datetime.datetime.now()}"
            self.slug = slugify(slug_str, allow_unicode=True)
        return super().save(*args, **kwargs)

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField( max_length=200,
        unique=True, blank=True, null=True, editable=True)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()

    def __str__(self):
        return self.title
    
    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = self.title.replace(" ", "-").replace(",", "")
        return super(Post, self).save(*args, **kwargs)

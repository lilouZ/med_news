from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    title = models.CharField(max_length=250, null=True)
    content = RichTextField(null=True)
    source = models.CharField(max_length=250, null=True)
    image = models.ImageField(upload_to='article_img/',null=True,blank=True)
    published_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE,null=True,blank=True)
    published_at = models.DateTimeField(auto_now=True)
    message = models.TextField(null=True)

    def __str__(self):
        return str(self.writer)



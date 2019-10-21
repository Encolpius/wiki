from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Sessions(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title 
    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'pk': self.pk})

class Comment(models.Model):
    post = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    def approve(self):
        self.approved_comment = True
        self.save()
    def __str__(self):
        return self.text
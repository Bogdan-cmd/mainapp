from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Creation(models.Model):
    title = models.CharField(max_length=100, verbose_name='titlu')
    content = models.TextField(verbose_name='conținut')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='creation_posts')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def total_likes(self):
        return self.likes.count()

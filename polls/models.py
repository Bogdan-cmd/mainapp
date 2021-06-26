from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Poll(models.Model):

    question = models.TextField(max_length=500)
    option_one = models.CharField(max_length=50,blank=False)
    option_two = models.CharField(max_length=50,blank=False)
    option_three = models.CharField(max_length=50,blank=False)
    option_four = models.CharField(max_length=50,blank=False)
    option_one_count = models.PositiveIntegerField(default=0)
    option_two_count = models.PositiveIntegerField(default=0)
    option_three_count = models.PositiveIntegerField(default=0)
    option_four_count = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    def total(self):
        return self.option_one_count + self.option_two_count + self.option_three_count + self.option_four_count

    def __str__(self):
        return self.question

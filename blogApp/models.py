from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):  # able to see in admin mode
        return self.name

    def get_absolute_url(self):  # able to reverse in terminal
        return reverse('home')


# this is the main class. Pictures are saved statically in a folder
class Post(models.Model):  # Null and auto if we don't have an image
    picture = models.ImageField(upload_to="images/", null=True, blank=True)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateField(auto_now_add=True)

# displays the posts information with author, title and date
    def __str__(self):  # object to str cast
        return str(self.author) + ' | ' + self.title + ' | ' + str(self.date)

# when post is clicked we will be redirected to the postDetails page.
    def get_absolute_url(self):
        return reverse('home')

class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.CharField(max_length=1000)

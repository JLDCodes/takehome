from django.contrib import admin
from .models import Post, Category


#  blog post to be accessed by admin area
admin.site.register(Post)
admin.site.register(Category)

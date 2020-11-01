from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blogApp.models import Post
from django.urls import reverse_lazy
from .forms import BlogForm

# Articles view
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-date', '-id']  # Order by date first, then by id, starting at earliest date


# Detailed view
class PostDetailView(DetailView):
    model = Post
    template_name = 'postDetails.html'


class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'updatePost.html'
    fields = ['title', 'category', 'body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'deletePost.html'
    success_url = reverse_lazy('home')

def FormView(request):
    form = BlogForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, "products/prod")

from django.shortcuts import render, get_object_or_404
from .models import Author, Post

# Create your views here.
def home(request):
    autores = Author.objects.all()
    return render(request, 'blog/home.html', {'autores': autores})


def author_projects(request, pk):
    posts = Post.objects.filter(author__id__contains=pk)
    return render(request, 'blog/posts/author_project.html', {'posts': posts})
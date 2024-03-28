from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Post

# Create your views here.
def home(request):
    autores = Author.objects.all()
    return render(request, 'blog/home.html', {'autores': autores})


def author_projects(request, pk, author_name):
    posts = Post.objects.filter(author__id__contains=pk)
    return render(request, 'blog/posts/author_project.html', {'p_k': pk, 'posts': posts, 'authorName': author_name})


def author_web_site(request, pk, author_name, project_name):
    project_dir = f'blog/templates/blog/posts/authors/{author_name}/{project_name}'
    html_file_path = '/src/html/main.html'
    
    with open(project_dir+html_file_path, 'r') as f:
        content = f.read()
    
    return HttpResponse(content)


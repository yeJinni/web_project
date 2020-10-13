from django.shortcuts import render
from .models import Post

def new(request):
    return render(request, 'new.html')

def create(request):
    gettitle = request.GET.get('title')
    getcontent = request.GET.get('content')

    post = Post(title=gettitle, content=getcontent)
    post.save()

    return render(request, 'create.html')

def main(request):
    return render(request, 'main.html')

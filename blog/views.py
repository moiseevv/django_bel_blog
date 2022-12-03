from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from blog.models import Post
from blog.forms import PostForm


def hello_world(request):
    return HttpResponse(f"<h1>Hi  {datetime.now()}</h1>")


def post_list(request):
    posts = Post.objects.all()
    context = {'items': posts}
    return render(request, 'blog/post_list.html', context)


def post_detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    context = {'post': post}
    return render(request, 'blog/post_detail.html', context)


def post_new(request):
    form = PostForm
    return render(request, 'blog/post_new.html', {'form': form})

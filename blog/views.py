from django.shortcuts import render, redirect, get_object_or_404
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
    if request.method == "GET":
        form = PostForm
        return render(request, 'blog/post_new.html', {'form': form})
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.create_date = datetime.now()
            post.publish_date = datetime.now()
            post.save()
            return redirect("post_detail", post_pk=post.pk)


def post_edit(request, post_pk):
    post = get_object_or_404(Post, pk = post_pk)
    if request.method == "GET":
        form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.create_date = datetime.now()
            post.publish_date = datetime.now()
            post.save()
            return redirect("post_detail", post_pk=post.pk)

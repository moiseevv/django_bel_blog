from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from blog.models import Post


def hello_world(request):
    return HttpResponse(f"<h1>Hi  {datetime.now()}</h1>")


def post_list(request):
    posts = Post.objects.all()
    context = {'items': posts}
    return render(request, 'blog/post_list.html', context)

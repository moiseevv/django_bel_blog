from django.urls import path
from blog.views import hello_world, post_list, post_detail

urlpatterns = [
    path('hello-world/', hello_world),
    path('post/detail/<int:post_pk>', post_detail, name='post_detail'),
    path('', post_list, name='post_list'),
]
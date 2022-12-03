from django.urls import path
from blog.views import hello_world, post_list, post_detail, post_new

urlpatterns = [
    path('hello-world/', hello_world),
    path('post_new/', post_new, name='post_new'),
    path('post/detail/<int:post_pk>', post_detail, name='post_detail'),
    path('', post_list, name='post_list'),
]
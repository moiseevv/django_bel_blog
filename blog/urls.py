from django.urls import path
from blog.views import hello_world, post_list, post_detail, post_new, post_edit

urlpatterns = [
    path('hello-world/', hello_world),
    path('post_new/', post_new, name='post_new'),
    path('post/detail/<int:post_pk>', post_detail, name='post_detail'),
    path('post/edit/<int:post_pk>', post_edit, name='post_edit'),
    path('', post_list, name='post_list'),
]
from django.urls import path
from blog.views import hello_world, post_list, post_detail, post_new, post_edit, post_delete, post_publish, high_reiting

urlpatterns = [
    path('hello-world/', hello_world, name='hi'),
    path('post_new/', post_new, name='post_new'),
    path('high/', high_reiting, name='high'),
    path('post/detail/<int:post_pk>', post_detail, name='post_detail'),
    path('post/publish/<int:post_pk>', post_publish, name='post_publish'),
    path('post/edit/<int:post_pk>', post_edit, name='post_edit'),
    path('post/delete/<int:post_pk>', post_delete, name='post_delete'),
    path('', post_list, name='post_list'),
]
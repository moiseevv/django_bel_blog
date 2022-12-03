from django.urls import path
from blog.views import hello_world, post_list

urlpatterns = [
    path('hello-world/', hello_world),
    path('', post_list, name='post_list')
]
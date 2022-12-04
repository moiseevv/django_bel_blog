from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=257, verbose_name='Статья')
    text = models.TextField(verbose_name='Текст')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    publish_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    publish = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"

class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текст комментария')
    publish_date = models.DateTimeField(verbose_name='Дата публикации комментария')

    def __str__(self):
        return self.text

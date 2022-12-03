from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=257, verbose_name='Статья')
    text = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    publish_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"

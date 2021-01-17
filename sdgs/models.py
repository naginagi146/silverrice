from django.db import models
from django.conf import settings
from accounts.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    text = models.TextField(("詳細"))
    created_at = models.DateTimeField(auto_now_add=True)
    user_tag = models.ForeignKey(User, blank=True, null=True, verbose_name=("コラボユーザー"), related_name='collabo_user', on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")

    def __str__(self):
        return self.text


class PostImage(models.Model):
    post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)
    modelimage = models.ImageField(("写真"),upload_to='post_images')



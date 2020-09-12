from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings


# Create your models here.
class ArticlePost(models.Model):
    # 作者信息
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # 文章标题
    title = models.CharField(max_length=100)

    # 文章正文
    body = models.TextField()

    # 文章创建时间
    created = models.DateTimeField(default=timezone.now())

    # 文章更新时间
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        # 按照创建时间倒叙
        ordering = ('-created',)

    def __str__(self):
        return self.title

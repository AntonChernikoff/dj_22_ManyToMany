
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Статья')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Фото', )

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Тэги'
        verbose_name_plural = 'Тэги статей'

    def __str__(self):
        return self.name


class ArticleScope(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='scopes')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    is_main = models.BooleanField(default=False)


from django.conf import settings
from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Article(models.Model):
    db_table = 'article'

    title = models.CharField(max_length=200, verbose_name='Article')
    text = models.TextField(verbose_name='Text')
    date = models.DateField(auto_now_add=True, verbose_name='Date')
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               verbose_name='Author',
                               on_delete=models.CASCADE)

    def __repr__(self):
        return '%s' % self.title

    def __str__(self):
        return '%s' % self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'


class Comment(MPTTModel):
    db_table = 'comment'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Author', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Text')
    date = models.DateField(auto_now_add=True, verbose_name='Date')
    parent = TreeForeignKey('self',
                            related_name='comment_children',
                            blank=True,
                            null=True,
                            on_delete=models.CASCADE,
                            verbose_name='Parent comment')
    article = models.ForeignKey(Article,
                                verbose_name='Articles',
                                on_delete=models.CASCADE,
                                related_name='comments')

    def __repr__(self):
        return '%s' % self.text

    def __str__(self):
        return '%s' % self.text

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

from django.contrib import admin
from .models import Article, Comment


@admin.register(Article)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

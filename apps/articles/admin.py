from django.contrib import admin

from .models import Article, Comment  # Добавили модели этого приложения и поместили в панель админа

admin.site.register(Article) 
admin.site.register(Comment)

from django.db import models
import datetime
from django.utils import timezone

class Article(models.Model):
    article_title =  models.CharField('Название статьи', max_length = 200, default = "Без названия")
    article_text = models.TextField('Текст статьи', default = "Тут пусто")
    article_author = models.CharField('Имя автора', max_length = 200,default="Без автора")
    pub_date = models.DateTimeField('Дата публикации',default = timezone.now())
    
    def __str__(self):
        return "{0}: {1}".format(self.article_author,self.article_title)

    def was_published_recently(self):
        return self.pub_date >= (timezone.now()  - datetime.timedelta(days = 7))
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete = models.CASCADE)
    author_name = models.CharField('Автор',max_length=100)
    comment_text = models.CharField('Содержание',max_length = 200)

    def __str__(self):
        return self.author_name
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
# Create your models here.

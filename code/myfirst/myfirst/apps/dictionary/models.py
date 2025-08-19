import datetime

from django.db import models

from django.utils import timezone

from django.utils.timezone import now

# Описание моделей, на основе которых создаётся БД

class Card(models.Model):
    word = models.CharField('слово', max_length = 50)
    definition = models.CharField('определение', max_length = 200)
    pub_date = models.DateTimeField('дата публикации', default=now, editable=False)
    #pub_date = models.DateTimeField('дата публикации', auto_now_add=True)

    def __str__(self):
        return self.word
    
    class Meta:
        verbose_name = 'Слово'
        verbose_name_plural = 'Слова'

class Dictionary(models.Model):
    dictionary_title = models.CharField('название статьи', max_length = 200)
    dictionary_text = models.TextField('текст статьи')
    pub_date = models.DateTimeField('дата публикации')

    def __str__(self):
        return self.dictionary_title

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days = 7))

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

class Comment(models.Model):
    dictionary = models.ForeignKey(Dictionary, on_delete = models.CASCADE)
    author_name = models.CharField('имя автора', max_length = 50)
    comment_text = models.CharField('текст комментария', max_length = 200)

    def __str__(self):
        return self.author_name
    
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
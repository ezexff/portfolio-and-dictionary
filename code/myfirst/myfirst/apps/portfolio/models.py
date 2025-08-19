from django.db import models

# Описание моделей, на основе которых создаётся БД

class Project(models.Model):
    project_title = models.CharField('название проекта', max_length = 60)
    project_description = models.TextField('описание проекта', max_length = 200)

    def __str__(self):
        return self.project_title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
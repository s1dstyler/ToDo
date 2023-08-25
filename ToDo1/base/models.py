from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=500, null=True, blank=True, verbose_name='Заголовок')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    complete = models.BooleanField(default=False, verbose_name='Выполнено')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']

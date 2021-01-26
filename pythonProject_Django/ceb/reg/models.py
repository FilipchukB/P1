from django.db import models


class Table1(models.Model):
    title = models.CharField('Назва', max_length=150)
    body = models.TextField('text')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'title'
        verbose_name_plural = 'titles'


class Table2(models.Model):
    title = models.CharField('Назва2', max_length=150)
    body = models.TextField('text')
    image = models.ImageField("foto", upload_to='reg/image')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'title2'
        verbose_name_plural = 'titles2'

from django.db import models


# Create your models here.


class Menu(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=200)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title

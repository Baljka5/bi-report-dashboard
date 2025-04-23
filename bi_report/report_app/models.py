from django.db import models


# Create your models here.


class Menu(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=200)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Link(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='links')
    title = models.CharField(max_length=200)
    url = models.URLField()

    def __str__(self):
        return self.title

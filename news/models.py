from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    image = models.ImageField()
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

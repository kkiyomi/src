from django.db import models

# Create your models here.


class MangaLink(models.Model):
    title = models.CharField(max_length=500)
    path = models.CharField(max_length=500)
    uid = models.CharField(max_length=50, default='N/A')
    language = models.CharField(max_length=50, default='N/A')

    def __str__(self):
        return f"{self.title}"


class MangaGroup(models.Model):
    name = models.CharField(max_length=500)
    uid = models.CharField(max_length=50)
    language = models.CharField(max_length=500)
    path = models.CharField(max_length=500)
    website = models.CharField(max_length=500)
    discord = models.CharField(max_length=500)
    rss = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.name} - {self.language}"

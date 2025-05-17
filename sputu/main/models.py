from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_published = models.DateField(auto_now_add=True)
image = models.ImageField(upload_to='news/', blank=True, null=True)


def __str__(self):
    return self.title


class Announcement(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_published = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Contest(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateField()
    attachment = models.FileField(upload_to='contests/', blank=True, null=True)

    def __str__(self):
        return self.title


class Program(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

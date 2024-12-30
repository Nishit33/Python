from django.db import models

# Create your models here.

class User(models.Model):
    Title = models.CharField(max_length=20)
    Code = models.TextField(max_length=100)
    Linenos = models.BooleanField(default=False)
    Language = models.CharField(max_length=20)
    Style = models.CharField(max_length=20)

    def __str__(self):
        return self.Title
        
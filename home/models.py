from re import L
from django.db import models
from django.utils import timezone
# Create your models here.

# 3 models -> comments, alumni,wall

class Comment(models.Model):
    author =  models.CharField(max_length=31)
    text = models.TextField()
    posted = models.DateTimeField(default=timezone.now)
    str_date = models.CharField(max_length=31, blank=True, null=True)

    def __str__(self):
        return f"{self.author} => {self.posted}"
    
    def save(self, *args,**kwargs):
        self.str_date = self.posted.strftime('%B %d %Y')
        super().save(*args,**kwargs)
    
    class meta:
        ordering = ['-posted']

class Alumni(models.Model):
    number = models.PositiveIntegerField(default=200000)

    def __str__(self):
        return self.number

class Wall(models.Model):
    user_stuff = models.JSONField()

    def __str__(self):
        return self.user_stuff
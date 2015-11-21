import datetime

from django.db import models

class Post (models.Model):#наследуется
    title=models.CharField(max_length=60)
    content=models.TextField()
    created_at=models.DateTimeField()
    views_count=models.IntegerField(default=0)
    def __str__(self):
        return self.title

class Comment (models.Model):
    name=models.CharField(max_length=60)
    message=models.TextField()
    created_at=models.DateTimeField(default=datetime.datetime.now)
    post=models.ForeignKey(Post)


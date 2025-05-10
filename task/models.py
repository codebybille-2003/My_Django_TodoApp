from django.db import models

# Create your models here.
class MyTask(models.Model):
    name=models.CharField(max_length=50)
    desc=models.TextField()

    def __str__(self):
        return self.name

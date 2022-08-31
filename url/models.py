from django.db import models

# Create your models here.



class Short(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    short = models.CharField(max_length=50, blank=True)
    url = models.URLField(max_length = 200)
  
    def __str__(self):
        return f'{self.title}'
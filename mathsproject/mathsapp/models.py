from django.db import models


# Create your models here.
class MyTable(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='pics')
    des = models.TextField()

    def __str__(self):
        return self.name

class NewTable(models.Model):
    name1 = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to='pics')
    des1 = models.TextField()

    def __str__(self):
        return self.name1

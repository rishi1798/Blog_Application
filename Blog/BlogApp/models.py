# Create your models here.
from django.db import models


class Blog(models.Model):
    class Meta:
        db_table='student'

    title = models.CharField(max_length=150)
    body = models.TextField()
    author = models.CharField(max_length=150)
    publish_date = models.DateField(null=True)
    update_date = models.DateField(null=True)
    image = models.ImageField(upload_to='uploads/', null=True)

    def __str__(self):
        return self.author + "-" +self.title

class Person(models.Model):
    class Meta:
        db_table='person'


    title = models.CharField(max_length=150,null=True)
    body = models.TextField(null=True)
    author = models.CharField(max_length=150,null=True)
    publish_date = models.DateField(null=True)
    update_date = models.DateField(null=True)
    image = models.ImageField(upload_to='uploads/',null=True)
    
    # def __str__(self):
        # return self.author + "-" +self.title

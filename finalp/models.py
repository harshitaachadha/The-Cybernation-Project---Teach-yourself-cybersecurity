from django.db import models

class user(models.Model):

    name = models.CharField(max_length=20)

    position = models.CharField(max_length=20)

    sal = models.IntegerField()

    user_name=models.CharField(max_length=10)

    password=models.IntegerField()

    def __str__(self):
        return self.name

from django.db import models


class Guest(models.Model):
    name = models.TextField()
    date = models.DateField(auto_now_add=True)
    message = models.TextField(max_length=200)

    def __str__(self):
        return self.name

    @staticmethod
    def submitted(name, message):
        Guest(name=name, message=message).save()
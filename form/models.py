from django.db import models


class Data(models.Model):
    datetime = models.DateTimeField(auto_now=True)
    data = models.JSONField()

    def __str__(self):
        return str(self.datetime)


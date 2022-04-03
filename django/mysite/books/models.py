import datetime

from django.db import models
from django.utils import timezone


class select_book(models.Model):
    category = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    writer = models.CharField(max_length=50)

    def __str__(self):  # __unicode__ on Python 2
        return self.category + '/ ' + self.title + '/ ' + self.writer

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
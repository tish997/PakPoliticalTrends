from django.db import models
from django.contrib.auth.models import User


class TrendsForm(models.Model):
    topic = models.CharField(max_length=100)
    to_date = models.DateField()
    from_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)

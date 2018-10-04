from __future__ import unicode_literals

from django.db import models

# Create your models here.
class deals(models.Model):
    name=models.TextField(null=False)
    image=models.TextField(null=False)
    rating=models.FloatField(null=False)
    link=models.TextField(null=False)
    actual_price=models.FloatField(null=False)
    discount=models.IntegerField(null=False)
    location=models.TextField(null=False)

class stats(models.Model):
    api_hits=models.IntegerField(null=False, default=0)
    def __unicode__(self):
        return str(self.api_hits)
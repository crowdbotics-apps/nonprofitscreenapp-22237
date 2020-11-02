from django.conf import settings
from django.db import models


class Call(models.Model):
    "Generated Model"
    placecall = models.ManyToManyField(
        "call.Phone",
        related_name="call_placecall",
    )
    history = models.BigIntegerField(
        null=True,
        blank=True,
    )
    callorigin = models.BigIntegerField(
        null=True,
        blank=True,
    )


# Create your models here.

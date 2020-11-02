from django.conf import settings
from django.db import models


class Phone(models.Model):
    "Generated Model"
    call = models.ManyToManyField(
        "phone.Call",
        blank=True,
        related_name="phone_call",
    )


# Create your models here.

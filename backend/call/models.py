from django.conf import settings
from django.db import models


class Phone(models.Model):
    "Generated Model"
    placecall = models.ForeignKey(
        "home.CustomText",
        on_delete=models.CASCADE,
        related_name="phone_placecall",
    )


# Create your models here.

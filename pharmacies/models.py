from django.db import models
from common.models import CommonModel

class Pharmacy(models.Model):
    title = models.CharField(
        verbose_name="약국명",
        max_length=100,
    )

    callNumber = models.CharField(
        verbose_name="연락처",
        max_length=20,
        null=True,
    )

    address = models.CharField(
        verbose_name="주소",
        max_length=140,
    )

    coordinate_X = models.CharField(
        max_length=40,
    )

    coordinate_Y = models.CharField(
        max_length=40,
    )
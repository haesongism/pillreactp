from django.db import models
from common.models import CommonModel

class Pharmacy(CommonModel):
    title = models.CharField(
        verbose_name="약국명",
        max_length=100,
    )

    address = models.CharField(
        verbose_name="주소",
        max_length=140,
    )

    callNumber1 = models.CharField(
        verbose_name="연락처1",
        max_length=20,
    )

    callNumber2 = models.CharField(
        verbose_name="연락처2",
        max_length=20,
    )

    coordinate_X = models.CharField(
        max_length=40,
    )

    coordinate_Y = models.CharField(
        max_length=40,
    )
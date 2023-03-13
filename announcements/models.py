from django.db import models
from common.models import CommonModel

class Announcement(CommonModel):
    """ Model Difinition for Announcement """

    writer = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        null=False,
    )

    views = models.IntegerField(

    )

    title = models.CharField(
        max_length=140,
        null=False,
    )

    content = models.TextField(
        null=True,
    )

    def __str__(self) -> str:
        return self.title
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

    created_at = models.DateTimeField(
        verbose_name="작성일",
        auto_now_add=True,
        # 해당 object가 생성되었을 때를 필드의 값으로 설정해준다.   
    )

    updated_at = models.DateTimeField(
        verbose_name="수정일",
        auto_now=True,
        # 해당 object가 저장되었을 때를 필드의 값으로 설정해준다.
    )
    def __str__(self) -> str:
        return self.title
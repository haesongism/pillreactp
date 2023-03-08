from django.db import models
from common.models import CommonModel
# 추상화시킨 모델로 해당 모델에서 created_at, updated_at 속성을 가지고 올 수 있다.

class Review(CommonModel):
    """ Model Definition for Review """

    review_photo = models.ImageField(
        blank=True,
    )    

    writer = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )

    medicine = models.ForeignKey(
        "medicines.Medicine",
        blank=True,
        on_delete=models.CASCADE,
    )

    views = models.IntegerField(
        verbose_name="조회수",
    )
    title = models.CharField(
        max_length=140,
        verbose_name="제목",
        null=False,
    )

    content = models.TextField(
        verbose_name="내용",
        null=False,
    )

    def __str__(self) -> str:
        return self.title

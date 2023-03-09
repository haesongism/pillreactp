from django.db import models
from common.models import CommonModel
# 추상화시킨 모델로 해당 모델에서 created_at, updated_at 속성을 가지고 올 수 있다.
from django.core.validators import MinValueValidator, MaxValueValidator
# review의 rating을 정하기 위하여 validator을 사용, 내장기능이기 때문에 채택

class Review(CommonModel):
    """ Model Definition for Review """

    review_photo = models.ImageField(
        blank=True,
        null=True,
    )    

    writer = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        null=True,
        related_name='reviews',
    )

    medicine = models.ForeignKey(
        "medicines.Medicine",
        blank=True,
        on_delete=models.CASCADE,
        related_name='reviews',
    )

    views = models.IntegerField(
        verbose_name="조회수",
        default=0,
    )
    title = models.CharField(
        max_length=140,
        verbose_name="제목",
        null=False,
    )

    content = models.TextField(
        verbose_name="내용",
        null=True,
    )  

    rating = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        default=0,
    )
    # 내장 재공하는 Validator를 활용하여 점수의 min, max값을 설정
    
    def __str__(self) -> str:
        return self.title

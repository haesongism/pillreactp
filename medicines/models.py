from django.db import models

class Medicine(models.Model):

    """ Model Definition for Medicines """

    name = models.CharField(
        max_length=140,
        verbose_name = "의약품명",
        )
    # 약 이름

    basis = models.CharField(
        max_length=140,
        verbose_name = "주 성분",
        )
    # 주 성분

    effect = models.TextField(
        verbose_name = "약효",
    )
    # 효과

    caution = models.TextField(
        verbose_name = "주의사항",
    )
    # 주의사항

    cautionOtherMedicines = models.BooleanField(
        verbose_name="다른 의약품과 함께 복용 가능지 여부",
        default=True,
        help_text="해당 DB를 아직 확인하지 않았기 때문에 default값 임시 저장한 상태."
        )
    # 다른 약과 함께 복용 가능한지의 여부

    is_etc = models.BooleanField(
        verbose_name="전문의약품(True), 일반의약품(False)",
        default=True,
    )

    # 평균 평점을 출력해준다.
    def rating(self):
        count = self.reviews.count()
        if count == 0:
            return "No Reviews"
        else:
            total_rating = 0
            for review in self.reviews.all().values("rating"):
                total_rating += review["rating"]
            return round(total_rating / count, 2)
    
    def __str__(self) -> str:
        return self.name
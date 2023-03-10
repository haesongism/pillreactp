from django.db import models

class Medicine(models.Model):

    """ Model Definition for Medicines """
    class EtcChoices(models.TextChoices):
        ETC = "ETC", "전문의약품"
        OTC = "OTC", "일반의약품"

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

    cautionOtherMedicines = models.TextField(
        verbose_name="함께 복용 불가능한 의약품 목록",
        null=True,
        )
    # 다른 약과 함께 복용 가능한지의 여부

    
    etcChoices = models.CharField(
        verbose_name="전문의약품(ETC), 일반의약품(OTC)",
        choices=EtcChoices.choices,
        max_length=3,
        blank=True,
    )

    #reviewList = 

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
    
    # 연동된 review 수
    def reviews_count(self):
        count = self.reviews.count()
        if count == 0:
            return "No Reviews"
        else:
            return count;

    # 연동된 review title
    def reviews_titles(self):
        count = self.reviews.count()
        if count == 0:
            return "No Reviews"
        else:
            reviews_titleList = []
            for review in self.reviews.all().values("title"):
                reviews_titleList.append(review)
            return reviews_titleList



    def __str__(self) -> str:
        return self.name
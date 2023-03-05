from django.db import models

class CommonModel(models.Model):
    """ Common Model Definition """
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

    class Meta:
        # django에서 model을 configure할 때 사용
        abstract = True
        # 추상화하여 DB에 저장하지 않게 설정.
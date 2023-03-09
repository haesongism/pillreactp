from django.db import models
from django.contrib.auth.models import AbstractUser
# 처음부터 만들지 않기 위해 기본 제공되던 기능을 가진 class를 사용
# AbstractUser는 AbstractBaseUser, PermissionsMixin 두 개의 기본기능을 제공하는 class를 상속받고 있기 때문에
# 모든 기능을 상속받아 사용할 수 있게 된다.


class User(AbstractUser):
    # AbstractUser class의 코드를 직접 수정하는일은 없다.
    # Overwriting을 통해서 관리하는것이 베스트
    # ex) 팀원들의 접근성이 떨어지고, 버전관리시 매번 수정한 유저의 코드를 받아가야하는 번거로움 등.
    class GenderChoices(models.TextChoices):
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")
    
    first_name = models.CharField(
        max_length=150,
        editable=False,
        null=True,
        )
    
    last_name = models.CharField(
        max_length=150,
        editable=False,
        null=True,
        )
    # 성, 이름은 불필요하기 때문에 제거
    profile_photo = models.ImageField(blank=True)
    name = models.CharField(max_length=150, default="")

    gender = models.CharField(
        max_length= 10,
        choices=GenderChoices.choices,
        )
    
    user_medicines = models.ManyToManyField(
        "medicines.Medicine",
        blank=True,
        related_name='users',
        # related_name은 FK의 대상이 된 medicines에서 관련된 user에 접근할 때 사용된다.
        # 하나만 선택하면 안된다. FK는 one to many를 뜻한다.
    )



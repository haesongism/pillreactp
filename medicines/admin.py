from django.contrib import admin
from .models import Medicine

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    # admin.ModelAdmin 상속받아 사용, 데코레이터를 통해 admin패널에 Medicine model을 등록.
    # admin 패널에 효과적인 표기 방식을 적용 가능

    list_display = (
        "name",
        "basis",
        "cautionOtherMedicines",
        "rating",
    )
    # admin 패널에 표기할 속성

    list_filter = (
        "name",
        "basis",
        "cautionOtherMedicines",
    )
    # admin 패널에서 필터를 적용할 속성

    search_fields = (
        "basis__startswith",
    )
    # 검색창 활성화

    list_editable = (
        "cautionOtherMedicines",
    )
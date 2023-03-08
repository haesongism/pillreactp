from django.contrib import admin
from .models import Pharmacy

@admin.register(Pharmacy)
class PharmacyAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "callNumber",
        "address",
        "coordinate_X",
        "coordinate_Y",
    )

    list_filter = (
        "address",
    )

    # 추후 주소 기준으로 검색기능 추가할것.
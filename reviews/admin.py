from django.contrib import admin
from .models import Review
# Register your models here.

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "views",
        "writer",
        "medicine",
        "rating",
    )

    list_filter = (
        "rating",
    )

    search_fields = (
        "title",
        "medicine__name",
        "writer__username",
        # = : __exact
        # ^ : __startswith
        # nothing : __contain
        # FK로 연동된 medicine -> "medicines.Medicine" 를 통하여 해당 app models.py의 name을 기반으로 검색가능하다.
        # FK로 연동된 writer -> "users.User" 를 통하여 해당 app models.py의 username을 기반으로 검색가능하다.
    )   
    # 검색창 활성화
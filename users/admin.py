from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# User를 위한 admin class
from .models import User
# 해당 class가 user model을 관리

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # 일반 모델이 아닌 user를 다루는 model이기 때문에 상속받을 class에 다양한 기능이 필요하다.
    # 상속받은 UserAdmin class는 admin.ModelAdmin class와는 다르게 user를 다루는 기능들이 구현되어있다.
    fieldsets = (
        ("Profile",
            {
                "fields": ("profile_photo", "username","password","name","email", "gender"),
                            "classes":("wide",),
            },
        ),
        ("Permissions",
            {
                "fields": ("is_active","is_staff","is_superuser","groups","user_permissions"),
                            "classes":("collapse",),
            },
        
         ),
        ("Important dates",
            {
                "fields": ("last_login", "date_joined"),
                            "classes":("collapse",),
            }
        )
    )
    list_display = (
        "username", "email","name","is_staff"
    )
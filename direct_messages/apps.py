from django.apps import AppConfig


class DirectMessagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'direct_messages'
    verbose_name = "Direct Messages"
    # 패널 표기이름 _ 제거하고싶어서 verbose_name 속성으로 정정

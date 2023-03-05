from django.urls import path
from . import views

urlpatterns = [
    path("", views.see_all_reviews),
    path("<int:review_pk>", views.see_one_reviews),
    # <자료형:파라미터 이름> : url에서 변수를 받을 수 있다.
    ]
# 이미 config.urls.py를 타고 들어온 경로이기 때문에 ""부분은 "reviews/"와 같게 작동한다.

from django.urls import path
from . import views

urlpatterns = [
    path("", views.Users.as_view()),# 회원가입
    path("me", views.Me.as_view()),# 로그인한 회원정보
    path("log-in", views.LogIn.as_view()),
    path("log-out", views.LogOut.as_view()),
    path("change-password",views.ChangePassword.as_view()),
    path("@<str:username>", views.PublicUser.as_view()),
]
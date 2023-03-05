from django.db import models
from common.models import CommonModel

class ChatRoom(CommonModel):
    """ ChatRoom Model Definition """

    users = models.ManyToManyField(
        "users.User",
    )
    # ManytoMany로 여러 유저가 참여할 수 있게 세팅

    def __str__(self) -> str:
        return "Chatting Room."

class Message(CommonModel):
    """ Message Model Definition """
    text = models.TextField()
    user = models.ForeignKey(
        "users.User",
        null=True,
        blank=True, # admin 패널에서 유저 없이 메세지를 만들 수 있게
        on_delete=models.SET_NULL,
        # 한명이 나가더라도 유저만 삭제하고 메세지는 남게 세팅.
    )

    room = models.ForeignKey(
        "direct_messages.ChatRoom",
        on_delete=models.CASCADE,
    )
    # 채팅방이 삭제되면 메세지도 같이 삭제되게 FK, CASCADE로 연동

    def __str__(self) -> str:
        return f"{self.user} say : {self.text}"
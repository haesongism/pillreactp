from rest_framework.serializers import ModelSerializer
from .models import Announcement
from users.serializers import TinyUserSerializer

class AnnouncementSerializer(ModelSerializer):
    writer = TinyUserSerializer(read_only=True)
    
    class Meta:
        model = Announcement
        fields = (
            'pk',
            'writer',
            'views',
            'title',
            'content',
        )

class AnnouncementDetailSerializer(ModelSerializer):

    writer = TinyUserSerializer()

    class Meta:
        model = Announcement
        fields = "__all__"
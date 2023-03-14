from rest_framework.serializers import ModelSerializer
from .models import Medicine, Comment

class MedicineSerializer(ModelSerializer):
    class Meta:
        model = Medicine
        fields = (
            "name",
            "etcChoices",
            "rating",
        )


class MedicineDetailSerializer(ModelSerializer):
    class Meta:
        model = Medicine
        fields = (
            "name",
            "basis",
            "effect",
            "caution",
            "cautionOtherMedicines",
            "etcChoices",
            "rating",
            "reviews_count",
            "reviews_titles",
        )


class TinyMedicineSerializer(ModelSerializer):
    class Meta:
        model = Medicine
        fields = (
            'name',
            'etcChoices',
        )

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'medicine',
            'content',
            'created_at',
        )
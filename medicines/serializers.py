from rest_framework.serializers import ModelSerializer
from .models import Medicine, Comment
from reviews.serializers import ReviewListSerializer 

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'medicine',
            'content',
            'created_at',
        )

class MedicineSerializer(ModelSerializer):
    class Meta:
        model = Medicine
        fields = (
            "pk",
            "name",
            "etcChoices",
            "rating",
        )


class MedicineDetailSerializer(ModelSerializer):
    #comment = CommentSerializer(read_only=True, many=True)
    # Medicine과 Comment는 relationship이기 때문에 수동으로 연결해줘야한다. 
    reviews = ReviewListSerializer(read_only=True, many=True)
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
            "reviews",
        )


class TinyMedicineSerializer(ModelSerializer):
    class Meta:
        model = Medicine
        fields = (
            'name',
            'etcChoices',
        )


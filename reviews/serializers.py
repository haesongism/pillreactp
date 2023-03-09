from rest_framework import serializers
from .models import Review

""" 어떻게 json형태로 표현할것인지 정의 """

# 수동 테스트 코드
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        # Meta클래스를 선언한 후 model 변수에 Review를 넣어주면 자동으로 Review의 모델을 읽어서 Serializer를 구성해준다.
        fields = "__all__"
        # 표기할 데이터를 정한다.
        # exclude = (), 제외할 항목 선택
        # fields = (), 표기할 항목 선택


"""
# 수동 테스트 코드
from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    # read_only 옵션으로 유효성 검사에서 제외시킬 수 있다.
    title = serializers.CharField(
        required=True,
        max_length=140,
        )
    content = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    writer = serializers.CharField(read_only=True)
    medicine = serializers.CharField(read_only=True)
    rating = serializers.IntegerField()
    # model에서 정의한 데이터타입들을 그대로 정의해줘야 한다, 매우 반복적인 작업을 거쳐야한다.

    def create(self, validated_data):
        return Review.objects.create(**validated_data)
        #**는 데이터를 딕셔너리 형태로 호출한다.
        #함수의 파라미터에 데이터를 직접 적는 수고를 덜어준다.
    # create를 통해 post로 입력받은 유저인풋이 리뷰를 생성해 줄 수 있게되었다.

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.content = validated_data.get("content", instance.content)
        instance.save()
        return instance
"""

from .models import Review
# 모든 Review의 정보를 가져와서 출력하기 위해
from .serializers import ReviewListSerializer, ReviewDetailSerializer
# 커스텀 번역기 코드 import
from rest_framework.viewsets import ModelViewSet
# APIView 대체..
from rest_framework.decorators import api_view
# rest_framework를 사용하기 위한 데코레이터 세팅
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView

"""
class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewListSerializer
    queryset = Review.objects.all()
"""



#APIView를 활용한 데이터 관리 코드.

class Reviews(APIView):
    
    def get(self, request):
        all_reviews = Review.objects.all()
        serializer = ReviewListSerializer(all_reviews, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReviewDetailSerializer(data=request.data)
        # user가 제공하는 데이터를 가지고 오고 싶다면 받은 data를 넘겨야한다.
        # ReviewSerializser는 보안을 위해 일부 정보만 가질 수 있지만 
        # ReviewDetailSerializer는 __all__선언으로 인해 모든 데이터를 받을 수 있다.
        # 이로 인해 유효성 검사를 수행할 수 있다, 다만 기본적으로 선언된 serializer의 데이터 구조를 충족시켜야한다.
        if serializer.is_valid():
            new_review = serializer.save()
            serializer = ReviewDetailSerializer(new_review)
            # 유저에게서 받은 데이터를 활용하여 Review 인스턴스를 생성해준다.
            # serializers.py에서 class를 생성해주면 해당 부분에서 처리를 진행한다.
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class ReviewDetail(APIView):

    def get_object(self, pk):
        try:
            return Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            raise ModuleNotFoundError
    # django REST API의 컨벤션, API의 상세한 부분을 찾을 때는 해당 함수를 거쳐서 진행되게끔 작성하는게 좋다.

    def get(self, request, pk):
        serializer = ReviewDetailSerializer(self.get_object(pk))
        return Response(serializer.data)

    def put(self, request, pk):
        serializer = ReviewDetailSerializer(
            self.get_object(pk),
            data=request.data,
            partial=True,
            )
        if serializer.is_valid():
            updated_review = serializer.save()
            return Response(ReviewDetailSerializer(updated_review).data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(status=HTTP_204_NO_CONTENT)

# from django.http import JsonResponse
# 일반 스트링이 아닌 JsonResponse를 return해야 한다.
# from django.core import serializers
# QuerySet을 변환시켜주는 framework 

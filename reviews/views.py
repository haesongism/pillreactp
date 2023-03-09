from .models import Review
# 모든 Review의 정보를 가져와서 출력하기 위해
from .serializers import ReviewSerializer
# 커스텀 번역기 코드 import
from rest_framework.viewsets import ModelViewSet
# APIView 대체..
from rest_framework.decorators import api_view
# rest_framework를 사용하기 위한 데코레이터 세팅
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()



""" 
APIView를 활용한 데이터 관리 코드.

    class Reviews(APIView):
    
    def get(self, request):
        all_reviews = Review.objects.all()
        serializer = ReviewSerializer(all_reviews, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        # user가 제공하는 데이터를 가지고 오고 싶다면 받은 data를 넘겨야한다.
        # 데이터 검사를 위해 세팅을 했기 때문에 ReviewSerializer는 이미 데이터의 형태를 모두 알고 있다
        # 이로 인해 유효성 검사를 수행할 수 있다, 다만 기본적으로 선언된 serializer의 데이터 구조를 충족시켜야한다.
        if serializer.is_valid():
            new_review = serializer.save()
            # 유저에게서 받은 데이터를 활용하여 Review 인스턴스를 생성해준다.
            # serializers.py에서 class를 생성해주면 해당 부분에서 처리를 진행한다.
            return Response(ReviewSerializer(new_review).data)
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
        serializer = ReviewSerializer(self.get_object(pk))
        return Response(serializer.data)

    def put(self, request, pk):
        serializer = ReviewSerializer(
            self.get_object(pk),
            data=request.data,
            partial=True,
            )
        if serializer.is_valid():
            updated_review = serializer.save()
            return Response(ReviewSerializer(updated_review).data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(status=HTTP_204_NO_CONTENT)

# from django.http import JsonResponse
# 일반 스트링이 아닌 JsonResponse를 return해야 한다.
# from django.core import serializers
# QuerySet을 변환시켜주는 framework """

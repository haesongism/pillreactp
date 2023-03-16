from django.shortcuts import render
from rest_framework.views import APIView
from .models import Medicine, Comment
from .serializers import MedicineSerializer, MedicineDetailSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.exceptions import NotFound, NotAuthenticated, PermissionDenied
from reviews.serializers import ReviewListSerializer
from .models import Medicine
from django.db.models import Q
from django.core.paginator import Paginator

def search(request):
  content_list = Medicine.objects.all()
  search = request.GET.get('search','')
  if search:
    search_list = content_list.filter(
      Q(name__icontains = search),# | #제목
      #Q(body__icontains = search) | #내용
      #Q(writer__username__icontains = search) #글쓴이
    )
  paginator = Paginator(search_list,5)
  page = request.GET.get('page','')
  posts = paginator.get_page(page)
  board = Medicine.objects.all()

  return render(request, 'search.html',{'posts':posts, 'Board':board, 'search':search})



    
   




class Medicines(APIView):

    def get(self, request):
        try:
            page = request.query_params.get('page', 1)
            page = int(page)
        except ValueError:
            page = 1
        page_size = 10
        start = (page-1) * page_size
        end = start + page_size    
        all_Medicines = Medicine.objects.all()[start:end]
        serializer = MedicineSerializer(all_Medicines, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MedicineSerializer(data=request.data)
        if request.user.is_authenticated:
            return NotAuthenticated
        if not request.user.is_staff or not request.user.is_superuser:
            return PermissionDenied
        if serializer.is_valid():
            new_medicine = serializer.save(permission_writer=request.user)
            return Response(MedicineSerializer(new_medicine).data)
        else:
            return Response(serializer.errors)
        

class MedicineDetail(APIView):

    def get_object(self, pk):
        try:
            return Medicine.objects.get(pk=pk)
        except Medicine.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        serializer = MedicineDetailSerializer(self.get_object(pk))
        return Response(serializer.data)
    
    def put(self, request, pk):
        medicine = self.get_object(pk)
        if not request.user.is_authenticated:
            raise NotAuthenticated
        if not request.user.is_staff or not request.user.is_superuser:
            raise PermissionDenied
        serializer = MedicineDetailSerializer(
            self.get_object(pk),
            data=request.data,
            partial=True,
            )
        if serializer.is_valid():
            updated_medicine = serializer.save(permission_writer=request.user)
            return Response(MedicineDetailSerializer(updated_medicine).data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        medicine = self.get_object(pk)
        # 1. 유저가 아니면 삭제할 수 없다.
        if not request.user.is_authenticated:
            raise NotAuthenticated
        # 2. 작성자가 아니면 삭제할 수 없다.
        if not request.user.is_staff or not request.user.is_superuser:
            raise PermissionDenied
        medicine.delete()
        return Response(status=HTTP_204_NO_CONTENT)



class Comments(APIView):
    def get(self, request):
        all_Comments = Comment.objects.all()
        serializer = CommentSerializer(all_Comments, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            new_comment = serializer.save()
            return Response(CommentSerializer(new_comment).data)
        else:
            return Response(serializer.errors)
        # save하기 전에 serializer에서 user정보를 받아와야한다.


class MedicineReview(APIView):
    """ 리뷰에서 연동된 FK medicine을 활용하여 관련 리뷰 출력 """
    def get_object(self, pk):
        try:
            return Medicine.objects.get(pk=pk)
        except Medicine.DoesNotExist:
            raise NotFound
    
    def get(self, request, pk):
        try:
            page = request.query_params.get('page', 1)
            page = int(page)
        except ValueError:
            page = 1
        page_size = 10
        start = (page-1) * page_size
        end = start + page_size
        medicine = self.get_object(pk)
        serializer = ReviewListSerializer(
            medicine.reviews.all()[start:end],#[:]pagination! 엄청 심플하다. 사랑한다 장고
            many=True,
            )
        return Response(serializer.data)
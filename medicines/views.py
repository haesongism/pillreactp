from django.shortcuts import render
from rest_framework.views import APIView
from .models import Medicine, Comment
from .serializers import MedicineSerializer, MedicineDetailSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.exceptions import NotFound, NotAuthenticated


class Medicines(APIView):

    def get(self, request):
        all_Medicines = Medicine.objects.all()
        serializer = MedicineSerializer(all_Medicines, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MedicineSerializer(data=request.data)
        if serializer.is_valid():
            new_medicine = serializer.save()
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
        pass

    def delete(self, request, pk):
        pass


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
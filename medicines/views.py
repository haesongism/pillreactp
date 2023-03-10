from django.shortcuts import render
from rest_framework.views import APIView
from .models import Medicine
from .serializers import MedicineSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT

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
            raise HTTP_204_NO_CONTENT

    def get(self, request, pk):
        serializer = MedicineSerializer(self.get_obejct(pk))
        return Response(serializer.data)
    
    def put(self, request, pk):
        pass

    def delete(self, request, pk):
        pass

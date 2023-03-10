from django.shortcuts import render
from rest_framework.views import APIView
from .models import Medicine
from .serializers import MedicineSerializer
from rest_framework.response import Response

class Medicines(APIView):

    def get(self, request):
        all_Medicines = Medicine.objects.all()
        serializer = MedicineSerializer(all_Medicines, many=True)
        return Response(serializer.data)

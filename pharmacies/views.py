from django.shortcuts import render
from rest_framework.views import APIView
from .models import Pharmacy
from .serializers import PharmacySerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT

class Pharmacies(APIView):

    def get(self, request):
        all_Pharmacies = Pharmacy.objects.all()
        serializer = PharmacySerializer(all_Pharmacies, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PharmacySerializer(data=request.data)
        if serializer.is_valid():
            new_pharmacies = serializer.save()
            return Response(PharmacySerializer(new_pharmacies).data)
        else:
            return Response(serializer.errors)
        
class PharmacyDetail(APIView):
    def get_object(self, pk):
        try:
            return Pharmacy.objects.get(pk=pk)
        except Pharmacy.DoesNotExist:
            raise HTTP_204_NO_CONTENT

    def get(self, request, pk):
        serializer = PharmacySerializer(self.get_obejct(pk))
        return Response(serializer.data)
    
    def put(self, request, pk):
        pass

    def delete(self, request, pk):
        pass

"""

from .models import Pharmacy
import csv
data = None
file_dir = 'D:/db/'

def read_data(table_name):
    with open(file_dir + f'{table_name}.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        global data
        data = list(reader)
    return

def footer(table_name, class_name, bulk_list):
    class_name.objects.bulk_create(bulk_list)

    with open(file_dir + f'{table_name}.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
    return

def add_pharmacies(request):
    read_data('pharmacies')
    if not data:
        return HttpResponse('Nothing to update')
    
    arr=[]
    for row in data:
        arr.append(Pharmacy())

    footer('pharmecies', Pharmacy, arr)
    return HttpResponse('Pharmacies table updated')
    """
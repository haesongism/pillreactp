from rest_framework.views import APIView
from .models import Pharmacy
from .serializers import PharmacySerializer, PharmacyDetailSerializer
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, NotAuthenticated
from rest_framework.pagination import PageNumberPagination ,LimitOffsetPagination, CursorPagination

class PharmacyPagination(CursorPagination):
    page_size = 10 # 한 페이지에 표시될 아이템 수
    page_query_param = 'page' # 페이지 번호를 나타내는 get 매개 변수 이름
    page_size_query_param = 'per_page' # 페이지 크기를 나타내는 get 매개 변수 이름
    max_page_size = 100 # 페이지 크기의 최대 값

class Pharmacies(APIView):
    pagination_class = PharmacyPagination

    def get(self, request):
        all_Pharmacies = Pharmacy.objects.all()
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(all_Pharmacies, request)
        serializer = PharmacySerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)#Response(serializer.data)
    
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
            raise NotFound

    def get(self, request, pk):
        serializer = PharmacyDetailSerializer(self.get_object(pk))
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
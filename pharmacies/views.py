

from django.shortcuts import render
from django.http import HttpResponse

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
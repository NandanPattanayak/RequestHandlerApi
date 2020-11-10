from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import demoModels,demo2Model
from .serializers import demoModelsSerializer,demo2ModelsSerializer
import csv
from rest_framework import status
from collections import OrderedDict
from pyexcel_xls import get_data as xls_get
from pyexcel_xlsx import get_data as xlsx_get
import pandas as pd
import json
# Create your views here.

@api_view(["POST"])
def HomeView(request):
   if request.method == 'POST':
        accept_file = request.FILES['files']
        if (str(accept_file).endswith(".csv")):
            df = pd.read_csv(accept_file,encoding='cp1252')
            col= df.columns
            col_list = []
            for i in col:
                col_list.append(i)
            data = df.to_dict('records')
            for i in data:
                data = OrderedDict(i)
                # fd = list(data.items())
                my_list = []
                for k,v in data.items():
                   my_list.append(v)
                final_data = {
                        "name":"String",
                        "collections":{"type" : "FeatureCollection",
                        "features":[{
                            "type": "Feature",
                            "geometry":{
                            "type": "Point",
                            "Coordinates":[my_list[0], my_list[1]],
                            },
                            "properties": {
        
                            col_list[2]: my_list[2],
                            col_list[3]:my_list[3],
                            col_list[4]:my_list[4],
                            col_list[5]:my_list[5],
                            col_list[6]:my_list[6]
                             },
                             }]} 
                             }
                serializers = demoModelsSerializer(data=final_data)
                if serializers.is_valid():
                    serializers.save()
            all_data = demoModels.objects.all()
            serializers = demoModelsSerializer(all_data,many=True)
            return Response(serializers.data,status=status.HTTP_200_OK)
        
        elif (str(accept_file).split('.')[-1] == 'xlsx'):
            data = pd.read_excel(accept_file)
            col= data.columns
            col_list = []
            for i in col:
                col_list.append(i)
            data = xlsx_get(accept_file)
            final_data = {}
            for (k,v) in data.items():
                for i in v:
                    final_data = {
                            "name":"String",
                            "collections":{"type" : "FeatureCollection",
                            "features":[{
                                "type": "Feature",
                                "geometry":{
                                "type": "Point",
                                "Coordinates":[i[0],i[1]],
                                },
                                "properties": {
            
                                col_list[2]: i[2],
                                col_list[3]: i[3],
                                col_list[4]: i[4],
                                col_list[5]: i[5],
                                col_list[6]: i[6]
                                },
                                }]} 
                                }
                    print(final_data)
                    serializers = demoModelsSerializer(data=final_data)
                    if serializers.is_valid():
                        serializers.save()
            all_data = demoModels.objects.all()
            serializers = demoModelsSerializer(all_data,many=True)
            return Response(serializers.data,status=status.HTTP_200_OK)
        elif (str(accept_file).split('.')[-1] == 'xls'):
            data = pd.read_excel(accept_file)
            print(data)
            col= data.columns
            col_list = []
            for i in col:
                col_list.append(i)
            data = xls_get(accept_file)
            final_data = {}
            for (k,v) in data.items():
                for i in v:
                    final_data = {
                            "name":"String",
                            "collections":{"type" : "FeatureCollection",
                            "features":[{
                                "type": "Feature",
                                "geometry":{
                                "type": "Point",
                                "Coordinates":[i[0],i[1]],
                                },
                                "properties": {
            
                                col_list[2]: i[2],
                                col_list[3]: i[3],
                                col_list[4]: i[4],
                                col_list[5]: i[5],
                                col_list[6]: i[6]
                                },
                                }]} 
                                }
                    print(final_data)
                    serializers = demoModelsSerializer(data=final_data)
                    if serializers.is_valid():
                        serializers.save()
            all_data = demoModels.objects.all()  
            serializers = demoModelsSerializer(all_data,many=True)
            return Response(serializers.data,status=status.HTTP_200_OK)
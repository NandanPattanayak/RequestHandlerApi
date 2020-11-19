from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import demoModels,demo2Model,NewModel,final_model,aimapsModel
from .serializers import demoModelsSerializer,demo2ModelsSerializer ,NewModelsSerializer,final_modelSerializer,aimapsModelSerializer
import csv
from rest_framework import status
from collections import OrderedDict
from pyexcel_xls import get_data as xls_get
from pyexcel_xlsx import get_data as xlsx_get
import pandas as pd
import json
import pygeodesy
from pygeodesy import ellipsoidalVincenty as eV
# from .models import aimapsModel
# from .serializers import  aimapsModelSerializer

@api_view(['GET',"POST"])
def AimapsView(request):
    if request.method == "GET":
        data = aimapsModel.objects.all()
        serializers = aimapsModelSerializer(data,many=True)
        return Response(serializers.data)
        # return Response({"M":"Done"})
@api_view(['POST'])
def ShowParticularDataView(request,a):
    if request.method == "POST":
        print(a)
        data = testModel.objects.filter(item=a)
        serializers = ms(data)
        return Response(serializers.data)













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
                try:
                    if my_list[0]!='' and my_list[1]!='' and my_list[2]!='' and my_list[3]!=''and my_list[4]!='' and my_list[5]!='' and my_list[6]!='':
                        utm = pygeodesy.Utm(31, 'N', my_list[0],my_list[1])
                        ll = str(utm.toLatLon(eV.LatLon))
                        final_data = {
                        "name":"String",
                        "collections":{"type" : "FeatureCollection",
                        "features":[{
                            "type": "Feature",
                            "geometry":{
                            "type": "Point",
                            "Coordinates":[ll],
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
                    # print(final_data)
                    serializers = final_modelSerializer(data=final_data)
                    if serializers.is_valid():
                        serializers.save()
                except Exception as e:
                    print(e)
            all_data =  final_model.objects.all()
            serializers = final_modelSerializer(all_data,many=True)
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
                    try:
                        if i[0]!='' and i[1]!='' and i[2]!='' and i[3]!=''and i[4]!='' and i[5]!='' and i[6]!='':
                            utm = pygeodesy.Utm(31, 'N',i[0],i[1])
                            ll = str(utm.toLatLon(eV.LatLon))
                            final_data = {
                                "name":"String",
                                "collections":{"type" : "FeatureCollection",
                                "features":[{
                                    "type": "Feature",
                                    "geometry":{
                                    "type": "Point",
                                    "Coordinates":[ll],
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
                    
                        serializers = final_modelSerializer(data=final_data)
                        if serializers.is_valid():
                            serializers.save()
                    except Exception as e:
                        print(e)
            all_data =  final_model.objects.all()  
            serializers = final_modelSerializer(all_data,many=True)
            return Response(serializers.data,status=status.HTTP_200_OK)
        elif (str(accept_file).split('.')[-1] == 'xls'):
            data = pd.read_excel(accept_file)
            col= data.columns
            col_list = []
            for i in col:
                col_list.append(i)
            data = xls_get(accept_file)
            final_data = {}
            for (k,v) in data.items():
                for i in v:
                    try:
                        if i[0]!='' and i[1]!='' and i[2]!='' and i[3]!=''and i[4]!='' and i[5]!=''and i[6]!='':
                            utm = pygeodesy.Utm(31, 'N',i[0],i[1])
                            ll = str(utm.toLatLon(eV.LatLon))
                            print(ll)
                            final_data = {
                                "name":"String",
                                "collections":{"type" : "FeatureCollection",
                                "features":[{
                                    "type": "Feature",
                                    "geometry":{
                                    "type": "Point",
                                    "Coordinates":[ll],
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
                    
                        serializers = final_modelSerializer(data=final_data)
                        if serializers.is_valid():
                            serializers.save()
                    
                    except Exception as e:
                        print(e)
            all_data =  final_model.objects.all()  
            serializers = final_modelSerializer(all_data,many=True)
            return Response(serializers.data,status=status.HTTP_200_OK)


@api_view(["GET"])
def FetchDataView(request):
    if request.method == "GET":
        all_data = NewModel.objects.all()
        serializers = NewModelsSerializer(all_data,many=True)
    return Response(serializers.data,status=status.HTTP_200_OK)
































# @api_view(["POST"])
# def HomeView(request):
#    if request.method == 'POST':
#         accept_file = request.FILES['files']
#         if (str(accept_file).endswith(".csv")):
#             df = pd.read_csv(accept_file,encoding='cp1252')
#             col= df.columns
#             col_list = []
#             for i in col:
#                 col_list.append(i)
#             data = df.to_dict('records')
#             for i in data:
#                 data = OrderedDict(i)
#                 # fd = list(data.items())
#                 my_list = []
#                 for k,v in data.items():
#                    my_list.append(v)
#                 try:
#                     if my_list[0]!='' and my_list[1]!='' and my_list[2]!='' and my_list[3]!=''and my_list[4]!='' and my_list[5]!='' and my_list[6]!='':
#                         utm = pygeodesy.Utm(31, 'N', my_list[0],my_list[1])
#                         ll = str(utm.toLatLon(eV.LatLon))
#                         final_data = {
#                         "name":"String",
#                         "collections":{"type" : "FeatureCollection",
#                         "features":[{
#                             "type": "Feature",
#                             "geometry":{
#                             "type": "Point",
#                             "Coordinates":[ll],
#                             },
#                             "properties": {
        
#                             col_list[2]: my_list[2],
#                             col_list[3]:my_list[3],
#                             col_list[4]:my_list[4],
#                             col_list[5]:my_list[5],
#                             col_list[6]:my_list[6]
#                              },
#                              }]} 
#                              }
#                     # print(final_data)
#                     serializers = NewModelsSerializer(data=final_data)
#                     if serializers.is_valid():
#                         serializers.save()
#                 except Exception as e:
#                     print(e)
#             all_data = NewModel.objects.all()
#             serializers = NewModelsSerializer(all_data,many=True)
#             return Response(serializers.data,status=status.HTTP_200_OK)
        
#         elif (str(accept_file).split('.')[-1] == 'xlsx'):
#             data = pd.read_excel(accept_file)
#             col= data.columns
#             col_list = []
#             for i in col:
#                 col_list.append(i)
#             data = xlsx_get(accept_file)
#             final_data = {}
#             for (k,v) in data.items():
#                 for i in v:
#                     try:
#                         if i[0]!='' and i[1]!='' and i[2]!='' and i[3]!=''and i[4]!='' and i[5]!='' and i[6]!='':
#                             utm = pygeodesy.Utm(31, 'N',i[0],i[1])
#                             ll = str(utm.toLatLon(eV.LatLon))
#                             final_data = {
#                                 "name":"String",
#                                 "collections":{"type" : "FeatureCollection",
#                                 "features":[{
#                                     "type": "Feature",
#                                     "geometry":{
#                                     "type": "Point",
#                                     "Coordinates":[ll],
#                                     },
#                                     "properties": {
                
#                                     col_list[2]: i[2],
#                                     col_list[3]: i[3],
#                                     col_list[4]: i[4],
#                                     col_list[5]: i[5],
#                                     col_list[6]: i[6]
#                                     },
#                                     }]} 
#                                     }
                    
#                         serializers = NewModelsSerializer(data=final_data)
#                         if serializers.is_valid():
#                             serializers.save()
#                     except Exception as e:
#                         print(e)
#             all_data = NewModel.objects.all()  
#             serializers = NewModelsSerializer(all_data,many=True)
#             return Response(serializers.data,status=status.HTTP_200_OK)
#         elif (str(accept_file).split('.')[-1] == 'xls'):
#             data = pd.read_excel(accept_file)
#             col= data.columns
#             col_list = []
#             for i in col:
#                 col_list.append(i)
#             data = xls_get(accept_file)
#             final_data = {}
#             for (k,v) in data.items():
#                 for i in v:
#                     try:
#                         if i[0]!='' and i[1]!='' and i[2]!='' and i[3]!=''and i[4]!='' and i[5]!=''and i[6]!='':
#                             utm = pygeodesy.Utm(31, 'N',i[0],i[1])
#                             ll = str(utm.toLatLon(eV.LatLon))
#                             print(ll)
#                             final_data = {
#                                 "name":"String",
#                                 "collections":{"type" : "FeatureCollection",
#                                 "features":[{
#                                     "type": "Feature",
#                                     "geometry":{
#                                     "type": "Point",
#                                     "Coordinates":[ll],
#                                     },
#                                     "properties": {
                
#                                     col_list[2]: i[2],
#                                     col_list[3]: i[3],
#                                     col_list[4]: i[4],
#                                     col_list[5]: i[5],
#                                     col_list[6]: i[6]
#                                     },
#                                     }]} 
#                                     }
                    
#                         serializers = NewModelsSerializer(data=final_data)
#                         if serializers.is_valid():
#                             serializers.save()
                    
#                     except Exception as e:
#                         print(e)
#             all_data = NewModel.objects.all()  
#             serializers = NewModelsSerializer(all_data,many=True)
#             return Response(serializers.data,status=status.HTTP_200_OK)
               


























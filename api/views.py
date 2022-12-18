#from django.shortcuts import render
import logging

from django.forms import CharField
from unittest import result

from rest_framework import viewsets, authentication, permissions, status, generics, mixins 
from api import serializers
from api.models import CheckBox
from api.serializers import CheckBoxSerializer, DataSerializer
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from api.utils import Sum

logger = logging.getLogger('django')

class CheckBoxViewSet(viewsets.ModelViewSet):
    queryset = CheckBox.objects.all()
    serializer_class = CheckBoxSerializer

    @action(detail=False, methods=["get"])
    def limit(self, req, pk=None):
        try:
            params = req.query_params
        except:   
            logger.info('Params: %s', params)
        return Response({"result":params})

class CheckboxList(generics.ListCreateAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = CheckBox.objects.all()
    serializer_class = CheckBoxSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs): 
        return  self.create(request, *args, **kwargs) 

@api_view(['GET'])
def checkbox_list(req):
    checkboxes = CheckBox.objects.all()
    serializer = CheckBoxSerializer(checkboxes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def checkbox_detail(req, pk):
    try:
        checkbox = CheckBox.objects.get(id=pk)
        serializer = CheckBoxSerializer(checkbox)
    except CheckBox.DoesNotExist:
        return  Response ((f"error: Checkbox with id = {pk} if not found"), status = status.HTTP_404_NOT_FOUND)
    return Response(serializer.data)  

@api_view(['POST'])
def checkbox_create(req):
    serializer = CheckBoxSerializer(data=req.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)    

@api_view(['PUT'])
def checkbox_update(req, pk):
    try:
        checkbox = CheckBox.objects.get(id=pk)
        serializer = CheckBoxSerializer(checkbox, data=req.data)
        if serializer.is_valid():
            serializer.save()
    except CheckBox.DoesNotExist:
        return  Response ((f"error: Checkbox with id = {pk} if not found"), status = status.HTTP_404_NOT_FOUND)
    return Response(serializer.data)  

@api_view(['DELETE'])
def checkbox_delete(req, pk):
    checkbox = CheckBox.objects.get(id=pk)
    checkbox.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)   

class DataView(APIView):

    @staticmethod
    def get(req):
        serializer = DataSerializer(data=req.query_params)   
        serializer.is_valid(raise_exception=True)  
        params = serializer.validated_data
        return Response({"params": params}, status=status.HTTP_200_OK)   

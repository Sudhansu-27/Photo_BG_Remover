from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Image
from .serializers import *

# Create your views here.
@api_view(['GET', 'POST'])
def images_list(request):
    if request.method == 'GET':
        data = Image.objects.all()
        serializer = ImageSerializer(data , context={'request': request}, many=True)
        
        return Response(serializer.data)
    
    elif request.method == 'POST':
        print(request.data)
        serializer = ImageSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            # print(status.HTTP_201_CREATED)
            print("ok 2000")
            # print(s)
            print("Ok 3000")
            return Response(data= serializer.data, status=status.HTTP_201_CREATED)

            

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def images_rmbg_list(request):
    if request.method == 'GET':
        data = Image.objects.filter(id = 2)
        
        serializer = ImageSerializer(data , context={'request': request}, many=True)
            
        return Response(serializer.data)
    
    
@api_view(['PUT', 'DELETE'])
def images_detail(request, pk):
    try:
        image = Image.objects.get(pk=pk)
    except Image.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = ImageSerializer(image, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

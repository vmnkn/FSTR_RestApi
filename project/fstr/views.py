from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.response import Response
from .models import *
from .serializers import *


class PerevalViewSet(viewsets.ModelViewSet):
    queryset = Pereval.objects.all()
    serializer_class = PerevalAddSerializer

    def create(self, request, *args, **kwargs):
        image = ImagesSerializer(data=request.data)
        if image.is_valid():
            image.save()
            return Response(status=201)
        else:
            print('Ошибка')
            return Response({'error': 'validation error'}, status=400)


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer


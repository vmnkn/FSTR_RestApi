from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist


class PerevalViewSet(viewsets.ModelViewSet):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer


class PerevalList(ListAPIView):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer


@api_view(['POST'])
def submit_data(request):
    serializer = PerevalSerializer(data=request.image)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
def get_data(request, pk):
    try:
        pereval = Pereval.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response(status=404)

    serializer = PerevalSerializer(pereval)
    return Response(serializer.data)

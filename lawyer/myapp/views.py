from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Lawyer,State, City, Notary
from .serializers import LawyerSerializer, StateSerializer, CitySerializer, NotarySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET', 'POST'])
def lawyerView(request):
    if request.method == 'GET':
        details =Lawyer.objects.all()
        serializer = LawyerSerializer(details, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        serializer = LawyerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(['GET', 'POST'])
def stateView(request):
    if request.method == 'GET':
        details =State.objects.all()
        serializer = StateSerializer(details, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        serializer = StateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(['GET', 'POST'])
def cityView(request):
    if request.method == 'GET':
        details =City.objects.all()
        serializer = CitySerializer(details, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return Response(serializer.errors)


def notaryView(request):
    if request.method == 'GET':
        detail = Notary.objects.all()
        serializer = NotarySerializer(detail, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        serialzer = NotarySerializer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return JsonResponse(serialzer.data)
        else:
            return Response(serialzer.errors)

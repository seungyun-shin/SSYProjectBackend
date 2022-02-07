from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import Record
from .products import products
from .serializers import RecordSerializer 

from django.http import JsonResponse
from rest_framework.response import Response

@api_view(['GET'])
def getRoute(request):
    return JsonResponse('SSY PROJECT API', safe=False)
    
@api_view(['GET'])
def getRecords(request):
    records = Record.objects.all().order_by('-createdAt')
    serializer = RecordSerializer(records, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getRecord(request, pk):

    record = Record.objects.get(_id=pk)

    record.visit_count = record.visit_count + 1
    record.save()

    serializer = RecordSerializer(record, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def createRecord(request):

    user = request.user

    record = Record.objects.create(
        user=user,
        title='empty record',
        category='etc',
        contents='empty',
        visit_count=0
    )

    serializer = RecordSerializer(record, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateRecord(request, pk):
    data = request.data
    record = Record.objects.get(_id=pk)

    record.title = data['title']
    record.category = data['category']
    record.contents = data['contents']
    # record.visit_count = data['visit_count']

    record.save()

    serializer = RecordSerializer(record, many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteRecord(request, pk):
    record = Record.objects.get(_id=pk)
    record.delete()
    return Response('Producted Deleted')

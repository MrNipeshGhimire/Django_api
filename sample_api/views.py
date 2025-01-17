from django.shortcuts import render
from rest_framework.views import APIView
from .models import Students
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class StudentView(APIView):

    def get(self,request):
        students = Students.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
    def post(self, request):
       serializer = StudentSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       else:
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       




        


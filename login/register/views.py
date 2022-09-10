from django.shortcuts import render

# Create your views here.
# from django.http import JsonResponse
from django.shortcuts import render
from register.models import Student
from rest_framework.response import Response
from rest_framework.decorators import  api_view
from .serilaizer import StudentSerializer

# Create your views here.


@api_view(['GET'])
def index(request):
    students = Student.objects.all()
    serialStudents = StudentSerializer(students,many=True)
    return Response(serialStudents.data)

@api_view(['GET'])
def studentView(request,pk):
    student = Student.objects.get(id=pk)
    serialStudent = StudentSerializer(student,many=False)
    return Response(serialStudent.data)

@api_view(['POST'])
def studentAdd(request):
    serialdata = StudentSerializer(data=request.data)
    if serialdata.is_valid():
        serialdata.save()
    return Response(serialdata.data)


@api_view(['POST'])
def studentUpdate(request,pk):
    student = Student.objects.get(id=pk)
    serialstudent = StudentSerializer(instance=student,data=request.data)
    if serialstudent.is_valid():
        serialstudent.save()

    return Response(serialstudent.data)

@api_view(['DELETE'])
def studentDelete(request,pk):
    student = Student.objects.get(id=pk)
    student.delete()
    students = Student.objects.all()
    serialStudents = StudentSerializer(students, many=True)
    return Response(serialStudents.data)
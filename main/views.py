from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Mentor, Mentee
from .serializers import MenteeSerializer, MentorSerializer

# Create your views here.

@api_view(["GET"])
def get_mentor(request, first_name: str) -> Response:
    mentor = Mentor.objects.get(first_name=first_name)
    serializer = MentorSerializer(data=mentor)
    if serializer.is_valid():
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(["POST"])
def create_mentor(request) -> Response:
    """create a new mentor object"""
    data = request['data']
    serializer = MentorSerializer(data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "created successfully"}, status=status.HTTP_201_CREATED)


@api_view(["GET"])
def list_mentors(request):
    mentors= Mentor.objects.all()
    serializer = MentorSerializer(mentors, many=True)
    if serializer.is_valid():
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(["GET"])
def get_mentee(request, first_name: str) -> Response:
    mentor = Mentee.objects.get(first_name=first_name)
    serializer = MenteeSerializer(data=mentor)
    if serializer.is_valid():
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(["POST"])
def create_mentee(request) -> Response:
    """create a new mentee object"""
    data = request['data']
    serializer = MenteeSerializer(data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "created successfully"}, status=status.HTTP_201_CREATED)


@api_view(["GET"])
def list_mentees(request):
    mentors= Mentee.objects.all()
    serializer = MenteeSerializer(mentors, many=True)
    if serializer.is_valid():
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
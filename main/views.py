from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Mentor, Mentee
from .serializers import MenteeSerializer, MentorSerializer

# Create your views here.

@api_view(["GET"])
def get_mentor(request, first_name: str) -> Response:
    try:
        mentor = Mentor.objects.get(first_name=first_name)
        serializer = MentorSerializer(data=mentor)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    except Mentor.DoesNotExist:
        return Response({"message": "object not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(["POST"])
def create_mentor(request) -> Response:
    """create a new mentor object"""
    data = request.get_json()
    mentor = Mentor.objects.create(**data)
    serializer = MentorSerializer(data=mentor)
    if serializer.is_valid():
        serializer.save()
        mentor.save()
        return Response({"message": "created successfully"}, status=status.HTTP_201_CREATED)


@api_view(["GET"])
def list_mentors(request):
    mentors= Mentor.objects.all()
    serializer = MentorSerializer(data=mentors, many=True)
    if serializer.is_valid():
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(["GET"])
def get_mentee(request, first_name: str) -> Response:
    try:
        mentor = Mentee.objects.get(first_name=first_name)
        serializer = MenteeSerializer(data=mentor)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    except Mentee.DoesNotExist:
        return Response({"message": "object does not exist"}, status=status.HTTP_404_NOT_FOUND)

@api_view(["POST"])
def create_mentee(request) -> Response:
    """create a new mentee object"""
    data = request.get_json()
    mentee = Mentee.objects.create(**data)
    serializer = MenteeSerializer(data=mentee)
    if serializer.is_valid():
        serializer.save()
        mentee.save()
        return Response({"message": "created successfully"}, status=status.HTTP_201_CREATED)


@api_view(["GET"])
def list_mentees(request):
    mentors= Mentee.objects.all()
    serializer = MenteeSerializer(data=mentors, many=True)
    if serializer.is_valid():
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def change_mentor(request):
    """change the mentor of a mentor based on the value passed in the request body and data"""
    actor = request.get_json()["actor"]
    if actor == "mentor":
        mentee_name = request.get_json()["mentee_name"]
        mentor = request.get_json()["mentor"]
        men = Mentor.objects.filter(first_name=mentee_name).update(mentor=mentor)
        men.save()
        serializer = MentorSerializer(data=men)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({"message":"object cannot be updated"}, status=status.HTTP_203_FAILED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["UPDATE"])
def update_mentee(request,name: str):
    """update a mentor object with required data"""
    try:
        mentee = Mentee.objects.get(last_name=name)
        data = request.get_json()
        mentee.update(data=data)
        serializer = MenteeSerializer(data=data)
        if serializer.is_valid():
            mentee.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Mentee.DoesNotExist:
        return Response({"message": "mentee object does not exist"}, status=status.HTTP_404_NOT_FOUND)
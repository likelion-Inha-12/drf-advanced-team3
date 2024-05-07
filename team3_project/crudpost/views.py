from django.shortcuts import render
import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from .models import *
from rest_framework.response import Response
from rest_framework import status
from .serializer import AssignmentSerializer, SubmissionSerializer, CategorySerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView

def create_assignment(request):
    #과제 생성
    assignement=Assignment(
        title=request.data.get('title'),
        deadline=request.data.get('deadline'),
        part=request.data.get('part'),
        tag=request.data.get('tag'),
        link = request.data.get('link'),
        content = request.data.get('content')
    )
    assignement.save()
    return JsonResponse({'message':'success'})

def create_submission(request):
    #제출물 생성
    submission = Submission(
        content = request.data.get('content'),
        link = request.data.get('link')
    )
    submission.save()
    return JsonResponse({'message':'success'})

def get_all_assignment(request):
    #생성되어 있는 전체 과제 목록 조회
    return 0

def get_assignment_part(request, part):
    assignments = Assignment.objects.filter(part=part) #특정 조건을 만족하는 객체들만 가져오는 메서드
    serializer = AssignmentSerializer(assignments, many=True, fields=['title', 'created_at', 'part'])
    return JsonResponse(serializer.data)

def get_assignment_tag(request, tag):
    assignments = Assignment.objects.filter(tag=tag)
    titles = [assignment.title for assignment in assignments ]
    return JsonResponse({'titles':titles})

class assignmentAPIView(APIView):

   def get_object(self, pk):
        assign=get_object_or_404(Assignment, pk=pk)
        return assign

   def get_assignment(self, request, pk):
        return 0

   def modify_assignment(self, request, pk):
        #특정 과제 내용 수정
        return 0

   def delete_assignment(self, request, pk):
        #특정 과제 삭제
        return 0

# Create your views here.

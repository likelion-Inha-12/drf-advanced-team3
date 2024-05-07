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
from rest_framework.response import Response


@api_view(['POST'])
def create_assignment(request):
    #과제 생성
    if request.method =='POST':

        assignement=Assignment(
            title=request.data.get('title'),
            deadline=request.data.get('deadline'),
            part=request.data.get('part'),
            tag=request.data.get('tag'),
            assign_github_link = request.data.get('assign_github_link'),
            assign_content = request.data.get('assign_content')
        )
        assignement.save()
    return JsonResponse({'message':'success'})

@api_view(['POST'])
def create_submission(request,assignment_id):
    assignment=get_object_or_404(Assignment, pk=assignment_id)
    submission = Submission(
        assignment_id = assignment,
        submit_content = request.data.get('submit_content'),
        submit_github_link = request.data.get('submit_github_link')
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
        assignment = get_object_or_404(Assignment, pk=pk)
        serializer = AssignmentSerializer(assignment)
        return Response(serializer.data)
    

   def modify_assignment(self, request, pk):
        #특정 과제 내용 수정
        return 0

   def delete_assignment(self, request, pk):
        #특정 과제 삭제
        assignment = get_object_or_404(Assignment, pk=pk)
        assignment.delete()
        return Response({"message": "delete"})


# Create your views here.

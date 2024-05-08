from django.shortcuts import render
import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from .models import *
from rest_framework.response import Response
from rest_framework import status
from .serializer import *
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.timezone import now

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

#api3 전체 조회
class AssignmentListAPIView(APIView):
    def get(self, request):
        assignments = Assignment.objects.all()
        categories = Category.objects.all()
        
        assignments_serializer = AssignmentSerializer(assignments, many=True)
        categories_serializer = CategorySerializer(categories, many=True)
        
        data = {
            'assignments': assignments_serializer.data,
            'categories': categories_serializer.data,
        }
        
        return Response(data)

def get_assignment_part(request, part):
    assignments = Assignment.objects.filter(part=part)

    if not assignments:
        return JsonResponse({'error': 'No assignments found with the given part.'}, status=404)

    data = []
    for assignment in assignments:
        assignment_data = {
            'part': assignment.part,
            'created_at': assignment.created_date, 
            'title': assignment.title,
        }
        data.append(assignment_data)
    return JsonResponse(data, safe=False)

def get_assignment_tag(request, tag):
    assignments = Assignment.objects.filter(tag=tag)

    if not assignments:
        return JsonResponse({'error': 'No assignments found with the given tag.'}, status=404)
    
    titles = [assignment.title for assignment in assignments ]
    return JsonResponse({'titles':titles})


class assignmentAPIView(APIView):

   def get_object(self, pk):
        assign=get_object_or_404(Assignment, pk=pk)
        return assign
   
   #api4 특정 과제 조회
   def get(self, request, pk):
        assignment = get_object_or_404(Assignment, pk=pk)
        serializer = AssignmentSerializer(assignment)
        return Response(serializer.data)

   def delete_assignment(self, request, pk):
        #특정 과제 삭제
        return 0

#api5 특정 과제 수정
@api_view(['PUT'])
def update_assignment(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)
    serializer = AssignmentSerializer(assignment, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "success"}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.

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
    if request.method =='POST':
        serializer = AssignmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message':'성공적으로 assignment가 생성되었습니다.'}, status=201)
        return JsonResponse(serializer.errors, status=400)
    return JsonResponse({'error': '유효하지 않은 요청입니다.'}, status=405)

@api_view(['POST'])
def create_submission(request, assignment_id):
    assignment = get_object_or_404(Assignment, pk=assignment_id)
    if request.method == 'POST':
        serializer = SubmissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(assignment_id=assignment)
            return JsonResponse({'message': '성공적으로 submission이 생성되었습니다.'}, status=201)
        return JsonResponse(serializer.errors, status=400)
    return JsonResponse({'error': '유효하지 않은 요청입니다.'}, status=405)


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
        return JsonResponse({'error': '해당 파트에 대응하는 assignment 정보가 없습니다.'}, status=404)

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
        return JsonResponse({'error': '해당 태그에 대응하는 assignment 정보가 없습니다.'}, status=404)
    
    titles = [assignment.title for assignment in assignments ]
    return JsonResponse({'titles':titles})


class assignmentAPIView(APIView):

   def get_object(self, pk):
        assign=get_object_or_404(Assignment, pk=pk)
        return assign
   
   #api4 특정 과제 조회
   def get(self, request, pk):
        assignment = self.get_object(pk)
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

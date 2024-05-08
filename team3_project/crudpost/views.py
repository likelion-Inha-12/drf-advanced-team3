from django.shortcuts import get_object_or_404
from .models import *
from rest_framework.response import Response
from rest_framework import status
from .serializer import *
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.timezone import now

#api1 과제 생성
@api_view(['POST'])
def create_assignment(request):
    if request.method =='POST':
        serializer = AssignmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'성공적으로 assignment가 생성되었습니다.'}, status=201)
        return Response(serializer.errors, status=400)
    return Response({'error': '유효하지 않은 요청입니다.'}, status=405)

#api2 제출물 생성
@api_view(['POST'])
def create_submission(request, assignment_id):
    assignment = get_object_or_404(Assignment, pk=assignment_id)
    if request.method == 'POST':
        serializer = SubmissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(assignment_id=assignment)
            return Response({'message': '성공적으로 submission이 생성되었습니다.'}, status=201)
        return Response(serializer.errors, status=400)
    return Response({'error': '유효하지 않은 요청입니다.'}, status=405)


#api3 전체 조회
class AssignmentListAPIView(APIView):
    def get(self, request):
        assignments = Assignment.objects.all()
        categories = assignments.order_by('tag').values_list('tag', flat=True).distinct()
        assignments_data = AssignmentSimpleSerializer(assignments, many=True).data
        
        response_data = {
            'categories': list(categories),
            'assignments': assignments_data
        }


class assignmentAPIView(APIView):

   def get_object(self, pk):
        assign=get_object_or_404(Assignment, pk=pk)
        return assign
   
   #api4 특정 과제 조회
   def get(self, request, pk):
        assignment = self.get_object(pk)
        serializer = AssignmentSerializer(assignment)
        return Response(serializer.data)
   #api6 특정 과제 삭제
   def delete(self, request, pk):
        assignment = self.get_object(pk)
        assignment.delete()
        return Response({'message':'deleted!'})

#api5 특정 과제 수정
@api_view(['PUT'])
def update_assignment(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)
    serializer = AssignmentSerializer(assignment, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "success"}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#api7 파트별 조회
@api_view(['GET'])
def get_assignment_part(request, part):
    assignments = Assignment.objects.filter(part=part)

    if not assignments:
        return Response({'error': '해당 파트에 대응하는 assignment 정보가 없습니다.'}, status=404)

    data = []
    for assignment in assignments:
        assignment_data = {
            'part': assignment.part,
            'created_at': assignment.created_date, 
            'title': assignment.title,
        }
        data.append(assignment_data)
    return Response(data, safe=False)


#api8 태그별 조회
@api_view(['GET'])
def get_assignment_tag(request, tag):
    assignments = Assignment.objects.filter(tag=tag)

    if not assignments:
        return Response({'error': '해당 태그에 대응하는 assignment 정보가 없습니다.'}, status=404)
    
    titles = [assignment.title for assignment in assignments ]
    return Response({'titles':titles})

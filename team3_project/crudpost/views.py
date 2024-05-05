from django.shortcuts import render
import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from .models import *
from rest_framework.response import Response
from rest_framework import status
from serializer import AssignmentSerializer, SubmissionSerializer, CategorySerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView

def create_assignment(request):
    #과제 생성
    return 0

def create_submission(request):
    #제출물 생성
    return 0

def get_all_assignment(request):
    #생성되어 있는 전체 과제 목록 조회
    return 0

def get_assignment_part(request):
    #파트별 과제 조회
    return 0

class aAssignmentAPIView(APIView):

    def get_object(self, pk):
        #특정 과제에 대해 불러오기
        return 0

    def get_assignment(self, request, pk):
        #특정 과제 내용 조회
        return 0

    def modify_assignment(self, request, pk):
        #특정 과제 내용 수정
        return 0

    def delete_assignment(self, request, pk):
        #특정 과제 삭제
        return 0


# Create your views here.

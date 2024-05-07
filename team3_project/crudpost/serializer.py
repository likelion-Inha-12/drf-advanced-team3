from rest_framework import serializers
from .models import Assignment, Submission, Category
from django.utils import timezone

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ['id', 'content', 'github_link', 'created_at']


class AssignmentSerializer(serializers.ModelSerializer):
    submissions = SubmissionSerializer(many=True)
    time_left = serializers.SerializerMethodField() #get_{field_name} 형식의 메서드를 정의하면 해당 메서드가 자동으로 호출돼서 해당 필드 값을 반환함. 
    submissions_count = serializers.SerializerMethodField()

    def get_time_left(self, obj):
        current_time=timezone.now()
        time_left = (obj.deadline - current_time) 
        hours, remainder = divmod(time_left.seconds, 3600)
        minutes, _ = divmod(remainder, 60) #마감일까지 남은 시, 분 구하기
        return {'days': time_left.days, 'hours':hours, 'minutes':minutes}
    
    def get_submissions_count(self, obj):
        return obj.submissions.count()
    
    class Meta:
        model = Assignment
        fields = ['id', 'title', 'created_at', 'deadline', 'part', 'tag', 'assign_github_link', 'assign_content', 'submissions', 'time_left','submissions_count']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']
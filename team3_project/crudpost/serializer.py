from rest_framework import serializers
from .models import Assignment, Submission, Category
from django.utils import timezone

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ['id', 'submit_content', 'submit_github_link', 'submit_date']


class AssignmentSerializer(serializers.ModelSerializer):
    submissions = serializers.SerializerMethodField()
    time_left = serializers.SerializerMethodField() #get_{field_name} 형식의 메서드를 정의하면 해당 메서드가 자동으로 호출돼서 해당 필드 값을 반환함. 
    submissions_count = serializers.SerializerMethodField()

    def get_submissions(self, obj):  # 추가
        submissions = obj.submission_set.all()  # 수정
        serializer = SubmissionSerializer(submissions, many=True)
        return serializer.data


    def get_time_left(self, obj):
        current_time=timezone.now()
        time_left = (obj.deadline - current_time) 
        hours, remainder = divmod(time_left.seconds, 3600)
        minutes, _ = divmod(remainder, 60) #마감일까지 남은 시, 분 구하기
        return {'days': time_left.days, 'hours':hours, 'minutes':minutes}
    
    def get_submissions_count(self, obj):
        return obj.submission_set.all().count()  # 수정
    
    class Meta:
        model = Assignment
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']
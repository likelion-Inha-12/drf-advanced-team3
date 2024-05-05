from rest_framework import serializers
from .models import Assignment, Submission, Category

class AssignmentSerializer(serializers.ModelSerializer):
    submissions = SubmissionSerializer(Submission)
    time_left = 0
    submissions_count = 0

    class Meta:
        model = Assignment
        fields = ['id', 'title', 'created_at', 'deadline', 'part', 'tag', 'link', 'content', 'submissions']

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ['id', 'content', 'github_link', 'created_at']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']
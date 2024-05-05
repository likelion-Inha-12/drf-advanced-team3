from rest_framework import serializers
from .models import Assignment, Submission, Category

class AssignmentSerializer(serializers.ModelSerializer):
    submissions = 0
    time_left = 0
    submissions_count = 0

    class Meta:
        model = Assignment
        fields = 0

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = 0

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']
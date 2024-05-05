from django.contrib import admin
from .models import Assignment, Submission
# Register your models here.
admin.site.register(Assignment) #Assigment 모델 등록
admin.site.register(Submission) # Submission 모델 등록
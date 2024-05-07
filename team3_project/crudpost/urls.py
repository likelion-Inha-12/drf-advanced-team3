from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('post/assign/', views.create_assignment),
    path('post/submission/<int:assignment_id>/', views.create_submission),
    path('post/part/<str:part>/', views.get_assignment_part),
    path('post/tag/<str:tag>/', views.get_assignment_tag),
    path('post/<int:pk>/', views.assignmentAPIView.as_view())
]
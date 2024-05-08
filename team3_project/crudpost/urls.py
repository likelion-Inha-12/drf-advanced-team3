from django.contrib import admin
from django.urls import path
from . import views
from .views import AssignmentListAPIView

urlpatterns = [
    #api1
    path('assign/', views.create_assignment),
    #api2
    path('submission/<int:assignment_id>/', views.create_submission),
    #api3
    path('assign/all/', AssignmentListAPIView.as_view(), name='assignment-list'),
    #api4, api6
    path('assign/<int:pk>/', views.assignmentAPIView.as_view()),
    #api5
    path('assign/update/<int:pk>/', views.update_assignment),
    #api7
    path('part/<str:part>/', views.get_assignment_part),
    #api8
    path('tag/<str:tag>/', views.get_assignment_tag),
]
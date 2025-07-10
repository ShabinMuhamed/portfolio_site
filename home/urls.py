from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view),
    path('about/', views.about_view),
    path('skills/', views.skills_view),
    path('projects/', views.projects_view,name='projects'),
    path('contact/', views.contact_view),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),

]
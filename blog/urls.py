from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('autor/<int:pk>/', views.author_projects, name='author_projects'),
]
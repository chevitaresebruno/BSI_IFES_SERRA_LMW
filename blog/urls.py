from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('autor/<int:pk>/<str:author_name>', views.author_projects, name='author_projects'),
    path('autor/<int:pk>/<str:author_name>/<str:project_name>', views.author_web_site, name='author_web_site')
]
from django.urls import path
from . import views

urlpatterns = [    
    path("task/", views.TodoView.as_view()),
    path("task/<int:pk>/", views.TodoView.as_view())
]
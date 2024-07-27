from django.urls import path
from . import views

urlpatterns = [
    path('view_answer_sheets/', views.view_answer_sheets, name='view_answer_sheets'),
    path('apply_revaluation/<int:pk>/', views.apply_revaluation, name='apply_revaluation'),
    path('search_marks/', views.search_marks, name='search_marks'),
    path('answer-sheets/', views.view_answer_sheets, name='view_answer_sheets'),
]

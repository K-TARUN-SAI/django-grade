from django.urls import path
from . import views

urlpatterns = [
    path('enter_marks/', views.enter_marks, name='enter_marks'),
    path('view_marks/', views.view_marks, name='view_marks'),
    path('edit_marks/<int:pk>/', views.edit_marks, name='edit_marks'),
    path('upload_answer_sheet/', views.upload_answer_sheet, name='upload_answer_sheet'),
    path('review_revaluation_requests/', views.review_revaluation_requests, name='review_revaluation_requests'),
]

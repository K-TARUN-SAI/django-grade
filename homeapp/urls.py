
from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name='home'),
    path('login', views.login, name='login'),
    path('login1/', views.login_view, name='login1'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('dashboard1/', views.student_dashboard, name='student_dashboard'),
    path('dashboard2/', views.admin_dashboard, name='admin_dashboard'),


]

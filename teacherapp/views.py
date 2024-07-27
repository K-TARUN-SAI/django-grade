from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.conf import settings
from django.core.mail import send_mail

def enter_marks(request):
    if request.method == 'POST':
        form = StudentMarkForm(request.POST)
        if form.is_valid():
            student = form.save()
            send_marks_email(student)
            return redirect('upload_success')
    else:
        form = StudentMarkForm()
    return render(request, 'teacherapp/enter_marks.html', {'form': form})

def view_marks(request):
    students = StudentMark.objects.all()
    return render(request, 'teacherapp/view_marks.html', {'students': students})

def edit_marks(request, pk):
    student = get_object_or_404(StudentMark, pk=pk)
    if request.method == 'POST':
        form = StudentMarkForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('view_marks')
    else:
        form = StudentMarkForm(instance=student)
    return render(request, 'teacherapp/edit_marks.html', {'form': form, 'student': student})

def upload_answer_sheet(request):
    if request.method == 'POST':
        form = AnswerPaperForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_successfully')
    else:
        form = AnswerPaperForm()
    return render(request, 'teacherapp/upload_answer_sheet.html', {'form': form})

def uploadsuccess(request):
    return render(request, 'teacherapp/upload_success.html')

def review_revaluation_requests(request):
    revaluation_requests = RevaluationRequest.objects.all()
    return render(request, 'teacherapp/review_revaluation_requests.html', {'revaluation_requests': revaluation_requests})

def send_marks_email(student):
    subject = 'Your Marks Have Been Uploaded'
    message = f'Hello {student.student_name},\n\nYour marks have been uploaded. Here are your marks:\n\n' \
              f'Subject 1: {student.subject1}\n' \
              f'Subject 2: {student.subject2}\n' \
              f'Subject 3: {student.subject3}\n' \
              f'Subject 4: {student.subject4}\n' \
              f'Subject 5: {student.subject5}\n' \
              f'Subject 6: {student.subject6}\n\n' \
              'Thank you!'
    recipient_list = [student.email]  # Ensure 'email' field exists in StudentMark model
    send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)
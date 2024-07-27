from django.shortcuts import render, get_object_or_404, redirect
from .forms import RevaluationRequestForm
from teacherapp.models import AnswerPaper, RevaluationRequest, StudentMark

# studentapp/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .forms import RevaluationRequestForm
from teacherapp.models import AnswerPaper, RevaluationRequest, StudentMark
from django.urls import reverse
from .forms import StudentIDForm


def view_answer_sheets(request):
    answer_papers = None
    student_id = request.GET.get('student_id')

    if student_id:
        try:
            student = StudentMark.objects.get(student_id=student_id)
            answer_papers = AnswerPaper.objects.filter(student=student)
        except StudentMark.DoesNotExist:
            student = None

    return render(request, 'studentapp/view_answer_sheets.html', {'answer_papers': answer_papers, 'student_id': student_id})
def apply_revaluation(request, pk):
    answer_paper = get_object_or_404(AnswerPaper, pk=pk)
    student = request.user.studentmark
    if request.method == 'POST':
        form = RevaluationRequestForm(request.POST)
        if form.is_valid():
            revaluation_request = form.save(commit=False)
            revaluation_request.student = student
            revaluation_request.answer_paper = answer_paper
            revaluation_request.save()
            return redirect('view_answer_sheets')
    else:
        form = RevaluationRequestForm()
    return render(request, 'studentapp/apply_revaluation.html', {'form': form, 'answer_paper': answer_paper})

def search_marks(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        try:
            student = StudentMark.objects.get(student_id=student_id)
            return render(request, 'studentapp/view_marks.html', {'student': student})
        except StudentMark.DoesNotExist:
            error_message = "Student ID not found."
            return render(request, 'studentapp/search_marks.html', {'error_message': error_message})
    return render(request, 'studentapp/search_marks.html')
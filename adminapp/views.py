# adminapp/views.py

import csv
from django.http import HttpResponse
from django.shortcuts import render
from teacherapp.models import StudentMark, AnswerPaper


def export_data(request):
    if request.method == 'POST':
        data_type = request.POST.get('data_type')
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="{data_type}.csv"'

        writer = csv.writer(response)

        if data_type == 'students':
            writer.writerow(
                ['Student ID', 'Student Name', 'Subject1', 'Subject2', 'Subject3', 'Subject4', 'Subject5', 'Subject6'])
            students = StudentMark.objects.all()
            for student in students:
                writer.writerow([
                    student.student_id, student.student_name, student.subject1,
                    student.subject2, student.subject3, student.subject4,
                    student.subject5, student.subject6
                ])
        elif data_type == 'answer_papers':
            writer.writerow(['Student ID', 'Student Name', 'Subject', 'File'])
            answer_papers = AnswerPaper.objects.select_related('student').all()
            for paper in answer_papers:
                writer.writerow([
                    paper.student.student_id, paper.student.student_name,
                    paper.subject, paper.file.url
                ])
        else:
            return render(request, 'adminapp/export_data.html', {'error': 'Invalid data type selected'})

        return response

    return render(request, 'adminapp/export_data.html')


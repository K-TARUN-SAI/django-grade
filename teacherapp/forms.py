from django import forms
from .models import StudentMark, AnswerPaper


class StudentMarkForm(forms.ModelForm):
    class Meta:
        model = StudentMark
        fields = ['student_id', 'student_name', 'email', 'subject1', 'subject2', 'subject3', 'subject4', 'subject5', 'subject6']



class AnswerPaperForm(forms.ModelForm):
    student_id = forms.ModelChoiceField(
        queryset=StudentMark.objects.all(),
        to_field_name="student_id",
        label="Student ID"
    )

    class Meta:
        model = AnswerPaper
        fields = ['student_id', 'subject', 'file']

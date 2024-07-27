from django import forms
from teacherapp.models import RevaluationRequest



class StudentIDForm(forms.Form):
    student_id = forms.CharField(label="Student ID", max_length=20)

class RevaluationRequestForm(forms.ModelForm):
    class Meta:
        model = RevaluationRequest
        fields = ['reason']

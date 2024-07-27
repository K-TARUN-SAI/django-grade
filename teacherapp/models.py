from django.db import models
from django.contrib.auth.models import User

class StudentMark(models.Model):
    student_id = models.CharField(max_length=20, unique=True)
    student_name = models.CharField(max_length=100)
    email = models.EmailField()  # Add email field
    subject1 = models.IntegerField()
    subject2 = models.IntegerField()
    subject3 = models.IntegerField()
    subject4 = models.IntegerField()
    subject5 = models.IntegerField()
    subject6 = models.IntegerField()

    def __str__(self):
        return f"{self.student_name} ({self.student_id})"



class AnswerPaper(models.Model):
    student = models.ForeignKey(StudentMark, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    file = models.FileField(upload_to='answer_papers/')

    def __str__(self):
        return f"{self.student.student_name} - {self.subject}"


class RevaluationRequest(models.Model):
    student = models.ForeignKey(StudentMark, on_delete=models.CASCADE)
    answer_paper = models.ForeignKey(AnswerPaper, on_delete=models.CASCADE)
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.student_name} - {self.answer_paper.subject}"

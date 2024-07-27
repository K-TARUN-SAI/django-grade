from django.contrib import admin
from .models import StudentMark, AnswerPaper, RevaluationRequest

# Register models with default admin interface
admin.site.register(StudentMark)
admin.site.register(AnswerPaper)
admin.site.register(RevaluationRequest)

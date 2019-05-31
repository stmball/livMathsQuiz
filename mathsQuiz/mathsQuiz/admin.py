from django.contrib import admin
from mathsQuiz.models import Quiz, Question, CompletionLog

admin.site.site_header = "Quiz Dashboard"
admin.site.site_title = "Quiz Dashboard"
admin.site.index_title = "Quiz Dashboard"

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(CompletionLog)
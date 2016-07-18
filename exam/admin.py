from django.contrib import admin
from .models import examType, subject, chapter, problem, comments

# Register your models here.
admin.site.register(examType)
admin.site.register(subject)
admin.site.register(chapter)
admin.site.register(problem)
admin.site.register(comments)

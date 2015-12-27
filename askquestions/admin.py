from django.contrib import admin
from askquestions.models import Question, Answer

class AnswerInLine(admin.StackedInline):
    model = Answer
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInLine]

# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)

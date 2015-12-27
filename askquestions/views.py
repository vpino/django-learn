from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, Http404
from askquestions.models import Question

def index(request):
    questions = Question.objects.all()
    return render_to_response('askquestions/index.html',
                                {'question': questions})

def question_detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render_to_response('askquestions/question_detail.html', {'question': question})
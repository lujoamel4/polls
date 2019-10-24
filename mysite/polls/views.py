""" Django views """
from django.http import HttpResponse
from django.shortcuts import render

from .models import Question


def index(request):
    """ Show all questions """
    latest_question_list = Question.objects.order_by('-pub_date')[:3]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    """ Show a single questions """
    question = Question.objects.get(id=question_id)
    context = {'question': question}
    return render(request, 'polls/poll.html', context)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
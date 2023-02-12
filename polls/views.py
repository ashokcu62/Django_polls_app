from django.shortcuts import render
from django.template import loader
from .models import Questions

# Create your views here.
from django.http import HttpResponse,HttpRequest,JsonResponse


def index(request:HttpRequest)->HttpResponse:
    latest_question_list=Questions.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context={
        "latest_question_list":latest_question_list
    }

    return HttpResponse(template.render(context,request))


def detail(request:HttpRequest, question_id)->HttpResponse:
    return HttpResponse(f"You're looking at question {question_id}")

def results(request:HttpRequest,question_id)->HttpResponse:
    return HttpResponse(f"response {question_id}")

def votes(request:HttpRequest,question_id)->HttpResponse:
    return HttpResponse(f"you are voting on question {question_id}")


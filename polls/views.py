from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.http import Http404
from .models import Questions

# Create your views here.
from django.http import HttpResponse,HttpRequest, Http404


def index(request:HttpRequest)->HttpResponse:
    latest_question_list=Questions.objects.order_by('-pub_date')[:5]
    context={
        "latest_question_list":latest_question_list
    }

    return render(request,"polls/index.html",context)


def detail(request:HttpRequest, question_id)->HttpResponse:
  
    question = get_object_or_404(Questions, pk=question_id)

    return render(request,'polls/details.html',{'question':question})

def results(request:HttpRequest,question_id)->HttpResponse:
    return HttpResponse(f"response {question_id}")

def votes(request:HttpRequest,question_id)->HttpResponse:
    return HttpResponse(f"you are voting on question {question_id}")


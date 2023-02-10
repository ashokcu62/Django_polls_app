from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpRequest,JsonResponse

def index(request:HttpRequest)->HttpResponse:
    return HttpResponse("hello its from  the polls app")
def details(request: HttpRequest)->JsonResponse:
    data={
        "id":1,
        "username":"ashok",
        "tutorial":"django"
    }
    return JsonResponse(data)
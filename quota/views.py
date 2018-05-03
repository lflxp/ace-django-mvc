from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View

# Create your views here.
def index(request):
    # return HttpResponse("hello world.")
    return render(request,"basic.html")

def detail(request,question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request,question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def myviews(request):
    result = ''
    if request.method == "POST":
        result = 'post'
        return HttpResponseRedirect('/success/')
    else:
        result = "get"
    return render(request,'form_template.html',{'result':result})

class MyView(View):
    modeling = "ok"

    def get(self,request):
        return HttpResponse("result "+self.modeling)
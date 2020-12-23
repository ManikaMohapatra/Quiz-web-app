from django.shortcuts import render
from app1.models import *

def showIndex(request):
    return render(request,'index.html')
def quizIndex(request):
    return render(request,'quiz.html',)
def gkIndex(request):
    questions = GkQuiz.objects.all()
    return render(request,'gk.html',{ 'questions': questions})
def scienceIndex(request):
    questions = ScienceQuiz.objects.all()
    return render(request,'science.html',{ 'questions': questions})
def sportsIndex(request):
    questions = SportsQuiz.objects.all()
    return render(request,'sports.html',{ 'questions': questions})

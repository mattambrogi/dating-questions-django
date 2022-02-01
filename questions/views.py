from django.shortcuts import render
from .models import Question
import random


def question(request):
    questions = Question.objects.all()
    question = random.choice(questions)
    context = {}
    context["data"] = question

    return render(request, "home.html", context)

def question_level(request, level):
    selected_level = level
    mapping = {'chill' : 1, 'deep': 2, 'deeper' : 3 }
    selected_level = mapping.get(level, "")    
    if level:
        questions = Question.objects.filter(level = selected_level)
    else: 
        questions = Question.objects.all()
    question = random.choice(questions)
    context = {}
    context["data"] = question
    context["selected_level"] = level
  

    return render(request, "home.html", context)
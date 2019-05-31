from django.shortcuts import render, get_object_or_404
from django.http import Http404
from mathsQuiz.models import Quiz, Question, CompletionLog

def index(request):
    return render(request, 'index.html')

def quiz(request, quizName):

    if request.method == 'POST':
        
        pass
        # TODO: Handle POST request for submission of completed quizzes
    
    else:

        quiz = get_object_or_404(Quiz, name=quizName)
        questions = quiz.Questions.all()

        contextList = {
            'quiz': quiz,
            'questions' : questions
        }

        return render(request, 'quiz.html', contextList)



def scoring(request):
    pass
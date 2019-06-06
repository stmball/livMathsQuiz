from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from django.utils import timezone
from mathsQuiz.models import Quiz, Question, CompletionLog, QuestionSet
from django.core.serializers import serialize
import json
from datetime import timedelta


def index(request):

    quizzes = Quiz.objects.filter(active=True)

    contextList = {
        'quizzes': quizzes
    }

    return render(request, 'index.html', contextList)


def quiz(request, quizName):

    if request.method == 'POST':
        postData = json.loads(request.body)
        newquiz = get_object_or_404(Quiz, name=postData['quizName'])

        newLog = CompletionLog(quiz=newquiz, name=postData['name'], score=postData['score'], timeTaken=timedelta(
            milliseconds=postData['delta']), dateComplete=timezone.now())
        newLog.save()
        return HttpResponse(status=201)
        # TODO: Handle POST request for submission of completed quizzes

    else:

        quiz = get_object_or_404(Quiz, name=quizName)
        questionSet = quiz.questionSet

        # Convert the questions to JSON format for use with the template Javascript code
        print(questionSet.questions.order_by('-title'))
        print("hello")
        questions = serialize("json", questionSet.questions.order_by('-title'))

        contextList = {
            'quiz': quiz,
            'questions': questions
        }

        return render(request, 'quiz.html', contextList)


def scoring(request):
    pass

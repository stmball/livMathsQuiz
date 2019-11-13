""" 
This file defines how Django deals with requests 
to the urls defined in urls.py.
"""


from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from django.utils import timezone
from mathsQuiz.models import Quiz, Question, CompletionLog, QuestionSet
from django.core.serializers import serialize
import json
from datetime import timedelta


def index(request):

    # Get visible quizzes
    quizzes = Quiz.objects.filter(visible=True)

    # Render the index html template with the relavant information
    contextList = {
        'quizzes': quizzes
    }

    return render(request, 'index.html', contextList)


def quiz(request, quizName):

    # The javascript code in the quiz html will make a post request to the quiz url
    # We load the data, get the relavent quiz and add a new completionlog to the database
    if request.method == 'POST':
        postData = json.loads(request.body)
        newquiz = get_object_or_404(Quiz, name=postData['quizName'])

        newLog = CompletionLog(quiz=newquiz, name=postData['name'], score=postData['score'], timeTaken=timedelta(
            milliseconds=postData['delta']), dateComplete=timezone.now())
        newLog.save()

        # Say everything's okay.
        return HttpResponse(status=201)

    # When visiting the webpage, most of the time we use a get request. For this we just
    # get the quiz, load the related question set, and pass the questions through to the
    # template.
    else:

        quiz = get_object_or_404(Quiz, name=quizName)
        questionSet = quiz.questionSet

        # Convert the questions to JSON format for use with the template Javascript code
        questions = serialize("json", questionSet.questions.order_by('pk'))

        contextList = {
            'quiz': quiz,
            'questions': questions
        }

        return render(request, 'quiz.html', contextList)

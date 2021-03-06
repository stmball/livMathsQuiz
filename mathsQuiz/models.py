from django.db import models
from urllib.parse import quote

# This file defines templates for the different data structures the website will work with. We use Django's model class methods to quickly define what type of data is expected.


# Go between model for Quizzes and Questions to allow for better organisation
class QuestionSet(models.Model):

    # Name for the question set
    name = models.CharField(
        max_length=30, help_text='The name for the question set')
    
    # Make Django know Question Sets are to be referred to by their name.
    def __str__(self):
        return self.name


class Quiz(models.Model):

    # Field for entering the name of a field.
    name = models.CharField(max_length=30, help_text='The name of the quiz.')

    # Organisational entry for question sets.
    questionSet = models.ForeignKey(
        QuestionSet, on_delete=models.CASCADE, related_name='quizzes')

    # Whether or not we show the user if their answer is right or wrong
    solutions = models.BooleanField(
        help_text='Tick this if you want solution feedback (eg You got the last question correct!)', default=True)

    # Whether or not a quiz is active or not
    visible = models.BooleanField(
        help_text='Tick this if the quiz is currently active', default=False)

    # This tells Django to refer to Quizzes by their titles.
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "quizzes"


class Question(models.Model):

    # Creaing a "Many to Many" relation with Question Sets - that is, one Question Set can use many Questions, and one Question may be used by many Qusetion Sets.
    questionSet = models.ManyToManyField(
        QuestionSet, related_name='questions', name='Question Set')

    # Field for the title of the question
    title = models.CharField(
        max_length=100, help_text='The title of the quesiton.')

    # Field for entering the text for a question.
    # TODO: Add MathML support to help text
    questionText = models.TextField(
        help_text='The question text written out, including any multiple choice answers.', name='Question Text')

    # Field for entering the correct answer for a question.
    # TODO: Does this need to be a CharField? If answers are all integers this can be changed.
    solution = models.CharField(
        max_length=100, help_text='The correct solution for the question')

    # This tells Django to refer to Questions by their title.
    def __str__(self):
        return self.title


# This model exists to log quiz completions, so they can be viewed by the quiz coordinator. No help text for this one as humans shouldn't be interacting with this model directly.

class CompletionLog(models.Model):

    # Creating a "Many to One" relation with Quizzes - each log belongs to exactly one quiz.
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    # Field for the server to enter in the name of the person who completed the quiz.
    name = models.CharField(
        max_length=100)

    # Field for the student's score.
    score = models.IntegerField()

    # Field for the student's time
    timeTaken = models.DurationField()

    # Field for when the quiz was taken. This is needed for filtering the logs later.
    dateComplete = models.DateTimeField()

    # This tells Django to refer to a log by the student that completed the quiz.
    def __str__(self):
        return self.name

    # TODO: Do we want to log what questions were completed correctly or not? Analytics?

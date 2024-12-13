from django.urls import path
from Quiz.views import start_quiz, quiz, result

urlpatterns = [
    path('', start_quiz, name='start_quiz'),
    path('quiz/', quiz, name='quiz'),
    path('result/', result, name='result'),
]














# from django.urls import path
# from Quiz.views import start_quiz, quiz, add_question

# urlpatterns = [
#     path('', start_quiz, name='start_quiz'),
#     path('quiz/', quiz, name='quiz'),
#     path('add-question/', add_question, name='add_question'),
# ]

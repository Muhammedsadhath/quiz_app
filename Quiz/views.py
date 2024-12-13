# from django.shortcuts import render, redirect
# from .models import QuesModel
# import random
# from .forms import AddQuestionForm

# # Start Quiz Page
# def start_quiz(request):
#     return render(request, 'Quiz/start_quiz.html')

# # Quiz Page
# def quiz(request):
#     if request.method == 'POST':
#         questions = QuesModel.objects.all()
#         score = 0
#         correct = 0
#         wrong = 0
#         total = len(questions)

#         for q in questions:
#             user_answer = request.POST.get(str(q.id))
#             if user_answer == q.ans:
#                 score += 10
#                 correct += 1
#             else:
#                 wrong += 1

#         context = {
#             'score': score,
#             'correct': correct,
#             'wrong': wrong,
#             'total': total,
#         }
#         return render(request, 'Quiz/result.html', context)

#     # Fetch 10 random questions
#     questions = list(QuesModel.objects.all())
#     random.shuffle(questions)
#     questions = questions[:10]

#     return render(request, 'Quiz/quiz.html', {'questions': questions})

# # Add Question (Admin Only)
# def add_question(request):
#     if not request.user.is_staff:
#         return redirect('start_quiz')
#     if request.method == 'POST':
#         form = AddQuestionForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('start_quiz')
#     else:
#         form = AddQuestionForm()

#     return render(request, 'Quiz/add_question.html', {'form': form})



from django.shortcuts import render, redirect
from .models import QuesModel
import random

# Start Quiz Page
def start_quiz(request):
    # Reset session data for a new quiz
    request.session['question_index'] = 0
    request.session['score'] = 0
    request.session['correct'] = 0
    request.session['wrong'] = 0

    # Shuffle and store 10 random questions in session
    questions = list(QuesModel.objects.all())
    random.shuffle(questions)
    questions = questions[:10]
    request.session['questions'] = [q.id for q in questions]

    return render(request, 'Quiz/start_quiz.html')

# Quiz Page (One Question at a Time)
def quiz(request):
    question_index = request.session.get('question_index', 0)
    question_ids = request.session.get('questions', [])
    
    if question_index >= len(question_ids):
        # If all questions are answered, redirect to result page
        return redirect('result')

    question = QuesModel.objects.get(id=question_ids[question_index])
    progress = int((question_index / len(question_ids)) * 100)

    if request.method == 'POST':
        selected_answer = request.POST.get('answer')
        if selected_answer == question.ans:
            request.session['score'] += 10
            request.session['correct'] += 1
        else:
            request.session['wrong'] += 1
        request.session['question_index'] += 1
        return redirect('quiz')

    return render(request, 'Quiz/quiz.html', {
        'question': question,
        'progress': progress
    })

# Result Page
def result(request):
    context = {
        'score': request.session.get('score', 0),
        'correct': request.session.get('correct', 0),
        'wrong': request.session.get('wrong', 0),
        'total': len(request.session.get('questions', [])),
    }
    return render(request, 'Quiz/result.html', context)

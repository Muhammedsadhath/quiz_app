
## Assumptions

1. **Single User:**
   - The app supports only one user, who can take the quiz.
   - The quiz does not require multiple users to be logged in at the same time.

2. **Question Management via Admin Panel:**
   - All questions are added and managed through the Django Admin interface.
   - Questions are multiple-choice, with four options (`op1`, `op2`, `op3`, `op4`).
   - Each question also includes a correct answer (`ans`).

3. **Randomized Question Selection:**
   - When the quiz is started, 10 random questions are selected from the database.
   - The set of questions is dynamic, and new questions can be added through the admin panel at any time.

4. **Timer and Progress Bar:**
   - The quiz starts with a timer that tracks the total time taken by the user to complete the quiz.
   - A progress bar is shown to indicate how much of the quiz the user has completed.

5. **Results Page:**
   - After completing the quiz, the user is shown a results page with:
     - Total score out of 10.
     - A breakdown of correct and incorrect answers.
     - Time taken to complete the quiz.

6. **Data Storage:**
   - The app uses SQLite as the database to store questions and user quiz results.
   - Questions are stored in the `Quiz.QuesModel` model with the fields: `question`, `op1`, `op2`, `op3`, `op4`, and `ans`.

7. **Admin User Setup:**
   - To manage the quiz questions, a superuser needs to be created via Django’s `createsuperuser` command.
   - The superuser can log in to the Django Admin interface at `/admin/` to add, edit, or delete questions.

8. **Questions File (Fixture):**
   - You can load predefined questions into the app using the `loaddata` command with a JSON fixture file (`questions.json`).
   - This file contains a set of 30 questions, each with 4 options and the correct answer specified.

9. **No Advanced Features:**
   - This app does not support features like user authentication, leaderboards, or advanced question types (e.g., images, videos).
   - The focus is on a simple multiple-choice quiz with basic result feedback.

## Features

- Admin panel to add, update, and delete quiz questions.
- Users can start a quiz, answer multiple-choice questions, and receive a score out of 10.
- Results page displaying the user's score and detailed information about each question.

## Requirements

- Python 3.8+
- Django 3.x
- SQLite (default database for development)

## Installation

## 1.Clone the repository:
git clone https://github.com/Muhammedsadhath/django-quiz-app.git

cd django-quiz-app

## 2.Create a virtual environment:
python -m venv venv

## 3.Activate the virtual environment:
## On Windows:
  .\venv\Scripts\activate

## On macOS/Linux:
  source venv/bin/activate

## 4.Install dependencies:
pip install -r requirements.txt

## 5.Apply migrations to set up the database:
python manage.py migrate

## 6.Create a superuser to access the Django admin panel:
python manage.py createsuperuser

## 7.Start the development server:
python manage.py runserver

Access the app at http://127.0.0.1:8000/. The admin panel can be accessed at http://127.0.0.1:8000/admin/
 

## Sample Data (Questions)
python manage.py loaddata questions.json

The questions.json file contains pre-defined questions with options and the correct answer.
You can load sample data (questions) into the app using the following command

## Admin Interface(you can also add questions via admin interface)
To add questions to the quiz, log in to the Django admin panel


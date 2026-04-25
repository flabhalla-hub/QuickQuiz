from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)
app.secret_key = "secret123"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    score = db.Column(db.Integer, default=0)


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), nullable=False)
    question = db.Column(db.String(200), nullable=False)
    choice1 = db.Column(db.String(100), nullable=False)
    choice2 = db.Column(db.String(100), nullable=False)
    choice3 = db.Column(db.String(100), nullable=False)
    answer = db.Column(db.String(100), nullable=False)


class Attempt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    count = db.Column(db.Integer, default=0)


@app.route('/')
def home():
    return redirect('/login')


@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        user = User(
            username=request.form['username'],
            email=request.form['email'],
            password=request.form['password']
        )
        db.session.add(user)
        db.session.commit()
        return redirect('/login')

    return render_template('register.html')


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(
            username=request.form['username'],
            password=request.form['password']
        ).first()

        if user:
            session['user'] = user.id
            return redirect('/dashboard')

    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/login')

    user = User.query.get(session['user'])
    categories = ["HTML", "CSS", "Flask", "Jinja2", "SQLAlchemy"]

    return render_template('dashboard.html', user=user, categories=categories)


@app.route('/quiz/<category>', methods=['GET','POST'])
def quiz(category):
    if 'user' not in session:
        return redirect('/login')

    # Vérifier les tentatives
    attempt = Attempt.query.filter_by(
        user_id=session['user'],
        category=category
    ).first()

    if attempt is None:
        attempt = Attempt(
            user_id=session['user'],
            category=category,
            count=0
        )
        db.session.add(attempt)
        db.session.commit()

    # Bloquer si 3 tentatives dépassées
    if attempt.count >= 3:
        user = User.query.get(session['user'])
        categories = ["HTML", "CSS", "Flask", "Jinja2", "SQLAlchemy"]
        return render_template('dashboard.html',
                               user=user,
                               categories=categories,
                               error=f"Vous avez dépassé 3 tentatives pour {category} !")

    questions = Question.query.filter_by(category=category).all()
    questions = random.sample(questions, min(10, len(questions)))

    if request.method == 'POST':
        score = 0
        for q in questions:
            if request.form.get(str(q.id)) == q.answer:
                score += 2

        user = User.query.get(session['user'])
        user.score += score

        # Incrémenter les tentatives
        attempt.count += 1
        db.session.commit()

        result = "Pass" if score >= 10 else "Fail"
        return render_template('result.html', score=score, result=result, category=category)

    return render_template('quiz.html',
                           questions=questions,
                           attempts_left=3 - attempt.count)


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')


if __name__ ==  '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)
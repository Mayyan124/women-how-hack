from flask import Flask, render_template
import os

app = Flask(__name__,
            template_folder='women who hack/frontend',
            static_folder='women who hack/frontend/static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/attacks')
def attacks():
    return render_template('attacks.html')

@app.route('/mysteries')
def mysteries():
    return render_template('mysteries.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/vision')
def vision():
    return render_template('vision.html')

@app.route('/profile')
@app.route('/Profile')
def profile():
    return render_template('profile.html')

@app.route('/login')
def login():
    return render_template('login.html')

# ─── קורסים ───────────────────────────────────────
@app.route('/courses')
def courses():
    return render_template('courses/index.html')

@app.route('/courses/languages')
def courses_languages():
    return render_template('courses/languages/index.html')

@app.route('/courses/languages/python')
def python_course():
    return render_template('courses/languages/python/index.html')

# ─── Level 1 ───────────────────────────────────────
@app.route('/courses/languages/python/lesson1')
def python_lesson1():
    return render_template('courses/languages/python/lesson1/index.html')

@app.route('/courses/languages/python/lesson2')
def python_lesson2():
    return render_template('courses/languages/python/Lesson2')

@app.route('/courses/languages/python/lesson3')
def python_lesson3():
    return render_template('courses/languages/python/Lesson3')

@app.route('/courses/languages/python/lesson4')
def python_lesson4():
    return render_template('courses/languages/python/Lesson4')

@app.route('/courses/languages/python/lesson5')
def python_lesson5():
    return render_template('courses/languages/python/Lesson5')

# ─── Level 2 ───────────────────────────────────────
@app.route('/courses/languages/python/lesson6')
def python_lesson6():
    return render_template('courses/languages/python/Lesson6')

@app.route('/courses/languages/python/lesson7')
def python_lesson7():
    return render_template('courses/languages/python/Lesson7')

@app.route('/courses/languages/python/lesson8')
def python_lesson8():
    return render_template('courses/languages/python/Lesson8')

@app.route('/courses/languages/python/lesson9')
def python_lesson9():
    return render_template('courses/languages/python/Lesson9')

@app.route('/courses/languages/python/lesson10')
def python_lesson10():
    return render_template('courses/languages/python/Lesson10')

# ─── Level 3 ───────────────────────────────────────
@app.route('/courses/languages/python/lesson11')
def python_lesson11():
    return render_template('courses/languages/python/Lesson11')

@app.route('/courses/languages/python/lesson12')
def python_lesson12():
    return render_template('courses/languages/python/Lesson12')

@app.route('/courses/languages/python/lesson13')
def python_lesson13():
    return render_template('courses/languages/python/Lesson13')

@app.route('/courses/languages/python/lesson14')
def python_lesson14():
    return render_template('courses/languages/python/Lesson14')

@app.route('/courses/languages/python/lesson15')
def python_lesson15():
    return render_template('courses/languages/python/Lesson15')

if __name__ == '__main__':
    app.run(debug=False)

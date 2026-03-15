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

# ─── Python ───────────────────────────────────────
@app.route('/courses/languages/python')
def python_course():
    return render_template('courses/languages/python/index.html')

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

# ─── C# ───────────────────────────────────────────
@app.route('/courses/languages/csharp')
def csharp_course():
    return render_template('courses/languages/csharp/index.html')

@app.route('/courses/languages/csharp/lesson1')
def csharp_lesson1():
    return render_template('courses/languages/csharp/lesson1/index.html')

@app.route('/courses/languages/csharp/lesson2')
def csharp_lesson2():
    return render_template('courses/languages/csharp/lesson2/index.html')

@app.route('/courses/languages/csharp/lesson3')
def csharp_lesson3():
    return render_template('courses/languages/csharp/lesson3/index.html')

@app.route('/courses/languages/csharp/lesson4')
def csharp_lesson4():
    return render_template('courses/languages/csharp/lesson4/index.html')

@app.route('/courses/languages/csharp/lesson5')
def csharp_lesson5():
    return render_template('courses/languages/csharp/lesson5/index.html')

@app.route('/courses/languages/csharp/lesson6')
def csharp_lesson6():
    return render_template('courses/languages/csharp/lesson6/index.html')

@app.route('/courses/languages/csharp/lesson7')
def csharp_lesson7():
    return render_template('courses/languages/csharp/lesson7/index.html')

@app.route('/courses/languages/csharp/lesson8')
def csharp_lesson8():
    return render_template('courses/languages/csharp/lesson8/index.html')

@app.route('/courses/languages/csharp/lesson9')
def csharp_lesson9():
    return render_template('courses/languages/csharp/lesson9/index.html')

@app.route('/courses/languages/csharp/lesson10')
def csharp_lesson10():
    return render_template('courses/languages/csharp/lesson10/index.html')

@app.route('/courses/languages/csharp/lesson11')
def csharp_lesson11():
    return render_template('courses/languages/csharp/lesson11/index.html')

@app.route('/courses/languages/csharp/lesson12')
def csharp_lesson12():
    return render_template('courses/languages/csharp/lesson12/index.html')

@app.route('/courses/languages/csharp/lesson13')
def csharp_lesson13():
    return render_template('courses/languages/csharp/lesson13/index.html')

@app.route('/courses/languages/csharp/lesson14')
def csharp_lesson14():
    return render_template('courses/languages/csharp/lesson14/index.html')

@app.route('/courses/languages/csharp/lesson15')
def csharp_lesson15():
    return render_template('courses/languages/csharp/lesson15/index.html')

@app.route('/courses/languages/csharp/lesson16')
def csharp_lesson16():
    return render_template('courses/languages/csharp/lesson16/index.html')

@app.route('/courses/languages/csharp/lesson17')
def csharp_lesson17():
    return render_template('courses/languages/csharp/lesson17/index.html')

@app.route('/courses/languages/csharp/lesson18')
def csharp_lesson18():
    return render_template('courses/languages/csharp/lesson18/index.html')

@app.route('/courses/languages/csharp/lesson19')
def csharp_lesson19():
    return render_template('courses/languages/csharp/lesson19/index.html')

@app.route('/courses/languages/csharp/lesson20')
def csharp_lesson20():
    return render_template('courses/languages/csharp/lesson20/index.html')

@app.route('/courses/languages/csharp/lesson21')
def csharp_lesson21():
    return render_template('courses/languages/csharp/lesson21/index.html')

@app.route('/courses/languages/csharp/lesson22')
def csharp_lesson22():
    return render_template('courses/languages/csharp/lesson22/index.html')

@app.route('/courses/languages/csharp/lesson23')
def csharp_lesson23():
    return render_template('courses/languages/csharp/lesson23/index.html')

@app.route('/courses/languages/csharp/lesson24')
def csharp_lesson24():
    return render_template('courses/languages/csharp/lesson24/index.html')

@app.route('/courses/languages/csharp/lesson25')
def csharp_lesson25():
    return render_template('courses/languages/csharp/lesson25/index.html')

@app.route('/courses/languages/csharp/lesson26')
def csharp_lesson26():
    return render_template('courses/languages/csharp/lesson26/index.html')

@app.route('/courses/languages/csharp/lesson27')
def csharp_lesson27():
    return render_template('courses/languages/csharp/lesson27/index.html')

@app.route('/courses/languages/csharp/lesson28')
def csharp_lesson28():
    return render_template('courses/languages/csharp/lesson28/index.html')

@app.route('/courses/languages/csharp/lesson29')
def csharp_lesson29():
    return render_template('courses/languages/csharp/lesson29/index.html')

@app.route('/courses/languages/csharp/lesson30')
def csharp_lesson30():
    return render_template('courses/languages/csharp/lesson30/index.html')

@app.route('/courses/languages/csharp/lesson31')
def csharp_lesson31():
    return render_template('courses/languages/csharp/lesson31/index.html')

@app.route('/courses/languages/csharp/lesson32')
def csharp_lesson32():
    return render_template('courses/languages/csharp/lesson32/index.html')

@app.route('/courses/languages/csharp/lesson33')
def csharp_lesson33():
    return render_template('courses/languages/csharp/lesson33/index.html')

@app.route('/courses/languages/csharp/lesson34')
def csharp_lesson34():
    return render_template('courses/languages/csharp/lesson34/index.html')

@app.route('/courses/languages/csharp/lesson35')
def csharp_lesson35():
    return render_template('courses/languages/csharp/lesson35/index.html')

@app.route('/courses/languages/csharp/lesson36')
def csharp_lesson36():
    return render_template('courses/languages/csharp/lesson36/index.html')

@app.route('/courses/languages/csharp/lesson37')
def csharp_lesson37():
    return render_template('courses/languages/csharp/lesson37/index.html')

@app.route('/courses/languages/csharp/lesson38')
def csharp_lesson38():
    return render_template('courses/languages/csharp/lesson38/index.html')

@app.route('/courses/languages/csharp/lesson39')
def csharp_lesson39():
    return render_template('courses/languages/csharp/lesson39/index.html')

@app.route('/courses/languages/csharp/lesson40')
def csharp_lesson40():
    return render_template('courses/languages/csharp/lesson40/index.html')

@app.route('/courses/languages/csharp/lesson41')
def csharp_lesson41():
    return render_template('courses/languages/csharp/lesson41/index.html')

@app.route('/courses/languages/csharp/lesson42')
def csharp_lesson42():
    return render_template('courses/languages/csharp/lesson42/index.html')

# ─── C# פרויקטים ──────────────────────────────────
@app.route('/courses/languages/csharp/project1')
def csharp_project1():
    return render_template('courses/languages/csharp/project1/index.html')

@app.route('/courses/languages/csharp/project2')
def csharp_project2():
    return render_template('courses/languages/csharp/project2/index.html')

@app.route('/courses/languages/csharp/project3')
def csharp_project3():
    return render_template('courses/languages/csharp/project3/index.html')

@app.route('/courses/languages/csharp/project4')
def csharp_project4():
    return render_template('courses/languages/csharp/project4/index.html')

@app.route('/courses/languages/csharp/project5')
def csharp_project5():
    return render_template('courses/languages/csharp/project5/index.html')

@app.route('/courses/languages/csharp/project6')
def csharp_project6():
    return render_template('courses/languages/csharp/project6/index.html')

@app.route('/courses/languages/csharp/project7')
def csharp_project7():
    return render_template('courses/languages/csharp/project7/index.html')

@app.route('/courses/languages/csharp/final-exam')
def csharp_final_exam():
    return render_template('courses/languages/csharp/final-exam/index.html')

if __name__ == '__main__':
    app.run(debug=False)

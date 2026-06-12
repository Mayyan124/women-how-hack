from flask import Flask, render_template, send_file
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
    path = os.path.join(app.template_folder, 'courses/languages/csharp/lesson1')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/csharp/lesson2')
def csharp_lesson2():
    path = os.path.join(app.template_folder, 'courses/languages/csharp/lesson2')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/csharp/lesson3')
def csharp_lesson3():
    path = os.path.join(app.template_folder, 'courses/languages/csharp/lesson3')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/csharp/lesson4')
def csharp_lesson4():
    path = os.path.join(app.template_folder, 'courses/languages/csharp/lesson4')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/csharp/lesson5')
def csharp_lesson5():
    path = os.path.join(app.template_folder, 'courses/languages/csharp/lesson5')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/csharp/lesson6')
def csharp_lesson6():
    path = os.path.join(app.template_folder, 'courses/languages/csharp/lesson6')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/csharp/lesson7')
def csharp_lesson7():
    path = os.path.join(app.template_folder, 'courses/languages/csharp/lesson7')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/csharp/lesson8')
def csharp_lesson8():
    path = os.path.join(app.template_folder, 'courses/languages/csharp/lesson8')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/csharp/lesson9')
def csharp_lesson9():
    path = os.path.join(app.template_folder, 'courses/languages/csharp/lesson9')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/csharp/lesson10')
def csharp_lesson10():
    path = os.path.join(app.template_folder, 'courses/languages/csharp/lesson10')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/csharp/lesson11')
def csharp_lesson11():
    path = os.path.join(app.template_folder, 'courses/languages/csharp/lesson11')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/csharp/lesson12')
def csharp_lesson12():
    path = os.path.join(app.template_folder, 'courses/languages/csharp/lesson12')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/csharp/lesson13')
def csharp_lesson13():
    path = os.path.join(app.template_folder, 'courses/languages/csharp/lesson13')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/csharp/lesson14')
def csharp_lesson14():
    path = os.path.join(app.template_folder, 'courses/languages/csharp/lesson14')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/csharp/lesson15')
def csharp_lesson15():
    path = os.path.join(app.template_folder, 'courses/languages/csharp/lesson15')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/csharp/lesson16')
def csharp_lesson16():
    path = os.path.join(app.template_folder, 'courses/languages/csharp/lesson16')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/csharp/lesson17')
def csharp_lesson17():
    path = os.path.join(app.template_folder, 'courses/languages/csharp/lesson17')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/csharp/lesson18')
def csharp_lesson18():
    path = os.path.join(app.template_folder, 'courses/languages/csharp/lesson18')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/csharp/lesson19')
def csharp_lesson19():
    path = os.path.join(app.template_folder, 'courses/languages/csharp/lesson19')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/csharp/lesson20')
def csharp_lesson20():
    path = os.path.join(app.template_folder, 'courses/languages/csharp/lesson20')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/csharp/lesson21')
def csharp_lesson21():
    path = os.path.join(app.template_folder, 'courses/languages/csharp/lesson21')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/csharp/lesson22')
def csharp_lesson22():
    path = os.path.join(app.template_folder, 'courses/languages/csharp/lesson22')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/csharp/lesson23')
def csharp_lesson23():
    path = os.path.join(app.template_folder, 'courses/languages/csharp/lesson23')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/csharp/lesson24')
def csharp_lesson24():
    path = os.path.join(app.template_folder, 'courses/languages/csharp/lesson24')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/csharp/lesson25')
def csharp_lesson25():
    path = os.path.join(app.template_folder, 'courses/languages/csharp/lesson25')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/csharp/lesson26')
def csharp_lesson26():
    path = os.path.join(app.template_folder, 'courses/languages/csharp/lesson26')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/csharp/lesson27')
def csharp_lesson27():
    path = os.path.join(app.template_folder, 'courses/languages/csharp/lesson27')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/csharp/lesson28')
def csharp_lesson28():
    path = os.path.join(app.template_folder, 'courses/languages/csharp/lesson28')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/csharp/lesson29')
def csharp_lesson29():
    path = os.path.join(app.template_folder, 'courses/languages/csharp/lesson29')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/csharp/lesson30')
def csharp_lesson30():
    path = os.path.join(app.template_folder, 'courses/languages/csharp/lesson30')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/csharp/lesson31')
def csharp_lesson31():
    path = os.path.join(app.template_folder, 'courses/languages/csharp/lesson31')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/csharp/lesson32')
def csharp_lesson32():
    path = os.path.join(app.template_folder, 'courses/languages/csharp/lesson32')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/csharp/lesson33')
def csharp_lesson33():
    path = os.path.join(app.template_folder, 'courses/languages/csharp/lesson33')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/csharp/lesson34')
def csharp_lesson34():
    path = os.path.join(app.template_folder, 'courses/languages/csharp/lesson34')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/csharp/lesson35')
def csharp_lesson35():
    path = os.path.join(app.template_folder, 'courses/languages/csharp/lesson35')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/csharp/lesson36')
def csharp_lesson36():
    path = os.path.join(app.template_folder, 'courses/languages/csharp/lesson36')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/csharp/lesson37')
def csharp_lesson37():
    path = os.path.join(app.template_folder, 'courses/languages/csharp/lesson37')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/csharp/lesson38')
def csharp_lesson38():
    path = os.path.join(app.template_folder, 'courses/languages/csharp/lesson38')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/csharp/lesson39')
def csharp_lesson39():
    path = os.path.join(app.template_folder, 'courses/languages/csharp/lesson39')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/csharp/lesson40')
def csharp_lesson40():
    path = os.path.join(app.template_folder, 'courses/languages/csharp/lesson40')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/csharp/lesson41')
def csharp_lesson41():
    path = os.path.join(app.template_folder, 'courses/languages/csharp/lesson41')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/csharp/lesson42')
def csharp_lesson42():
    path = os.path.join(app.template_folder, 'courses/languages/csharp/lesson42')
    return send_file(path, mimetype='text/html')

# ─── C# פרויקטים ──────────────────────────────────
@app.route('/courses/languages/csharp/project1')
def csharp_project1():
    path = os.path.join(app.template_folder, 'courses/languages/csharp/project1')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/csharp/project2')
def csharp_project2():
    path = os.path.join(app.template_folder, 'courses/languages/csharp/project2')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/csharp/project3')
def csharp_project3():
    path = os.path.join(app.template_folder, 'courses/languages/csharp/project3')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/csharp/project4')
def csharp_project4():
    path = os.path.join(app.template_folder, 'courses/languages/csharp/project4')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/csharp/project5')
def csharp_project5():
    path = os.path.join(app.template_folder, 'courses/languages/csharp/project5')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/csharp/project6')
def csharp_project6():
    path = os.path.join(app.template_folder, 'courses/languages/csharp/project6')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/csharp/project7')
def csharp_project7():
    path = os.path.join(app.template_folder, 'courses/languages/csharp/project7')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/csharp/final-exam')
def csharp_final_exam():
    path = os.path.join(app.template_folder, 'courses/languages/csharp/final exam')
    return send_file(path, mimetype='text/html')

# ─── JavaScript ───────────────────────────────────
@app.route('/courses/languages/javascript')
def javascript_course():
    path = os.path.join(app.template_folder, 'courses/languages/JavaScript/index.html')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/javascript/lesson1')
def javascript_lesson1():
    path = os.path.join(app.template_folder, 'courses/languages/JavaScript/lesson1')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/javascript/lesson2')
def javascript_lesson2():
    path = os.path.join(app.template_folder, 'courses/languages/JavaScript/lesson2')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/javascript/lesson3')
def javascript_lesson3():
    path = os.path.join(app.template_folder, 'courses/languages/JavaScript/lesson3')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/javascript/lesson4')
def javascript_lesson4():
    path = os.path.join(app.template_folder, 'courses/languages/JavaScript/lesson4')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/javascript/lesson5')
def javascript_lesson5():
    path = os.path.join(app.template_folder, 'courses/languages/JavaScript/lesson5')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/javascript/lesson6')
def javascript_lesson6():
    path = os.path.join(app.template_folder, 'courses/languages/JavaScript/lesson6')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/javascript/lesson7')
def javascript_lesson7():
    path = os.path.join(app.template_folder, 'courses/languages/JavaScript/lesson7')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/javascript/lesson8')
def javascript_lesson8():
    path = os.path.join(app.template_folder, 'courses/languages/JavaScript/lesson8')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/javascript/lesson9')
def javascript_lesson9():
    path = os.path.join(app.template_folder, 'courses/languages/JavaScript/lesson9')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/javascript/lesson10')
def javascript_lesson10():
    path = os.path.join(app.template_folder, 'courses/languages/JavaScript/lesson10')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/javascript/lesson11')
def javascript_lesson11():
    path = os.path.join(app.template_folder, 'courses/languages/JavaScript/lesson11')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/javascript/lesson12')
def javascript_lesson12():
    path = os.path.join(app.template_folder, 'courses/languages/JavaScript/lesson12')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/javascript/lesson13')
def javascript_lesson13():
    path = os.path.join(app.template_folder, 'courses/languages/JavaScript/lesson13')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/javascript/lesson14')
def javascript_lesson14():
    path = os.path.join(app.template_folder, 'courses/languages/JavaScript/lesson14')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/javascript/lesson15')
def javascript_lesson15():
    path = os.path.join(app.template_folder, 'courses/languages/JavaScript/lesson15')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/javascript/lesson16')
def javascript_lesson16():
    path = os.path.join(app.template_folder, 'courses/languages/JavaScript/lesson16')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/javascript/lesson17')
def javascript_lesson17():
    path = os.path.join(app.template_folder, 'courses/languages/JavaScript/lesson17')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/javascript/lesson18')
def javascript_lesson18():
    path = os.path.join(app.template_folder, 'courses/languages/JavaScript/lesson18')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/javascript/lesson19')
def javascript_lesson19():
    path = os.path.join(app.template_folder, 'courses/languages/JavaScript/lesson19')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/javascript/lesson20')
def javascript_lesson20():
    path = os.path.join(app.template_folder, 'courses/languages/JavaScript/lesson20')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/javascript/lesson21')
def javascript_lesson21():
    path = os.path.join(app.template_folder, 'courses/languages/JavaScript/lesson21')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/javascript/lesson22')
def javascript_lesson22():
    path = os.path.join(app.template_folder, 'courses/languages/JavaScript/lesson22')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/javascript/lesson23')
def javascript_lesson23():
    path = os.path.join(app.template_folder, 'courses/languages/JavaScript/lesson23')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/javascript/lesson24')
def javascript_lesson24():
    path = os.path.join(app.template_folder, 'courses/languages/JavaScript/lesson24')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/javascript/lesson25')
def javascript_lesson25():
    path = os.path.join(app.template_folder, 'courses/languages/JavaScript/lesson25')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/javascript/project1')
def javascript_project1():
    path = os.path.join(app.template_folder, 'courses/languages/JavaScript/project1')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/javascript/project2')
def javascript_project2():
    path = os.path.join(app.template_folder, 'courses/languages/JavaScript/project2')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/javascript/project3')
def javascript_project3():
    path = os.path.join(app.template_folder, 'courses/languages/JavaScript/project3')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/javascript/project4')
def javascript_project4():
    path = os.path.join(app.template_folder, 'courses/languages/JavaScript/project4')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/javascript/final-project')
def javascript_final_project():
    path = os.path.join(app.template_folder, 'courses/languages/JavaScript/final project')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/javascript/final-exam')
def javascript_final_exam():
    path = os.path.join(app.template_folder, 'courses/languages/JavaScript/final exam')
    return send_file(path, mimetype='text/html')

# ─── Java ─────────────────────────────────────────
@app.route('/courses/languages/java')
def java_course():
    path = os.path.join(app.template_folder, 'courses/languages/Java/index.html')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/java/lesson1')
def java_lesson1():
    path = os.path.join(app.template_folder, 'courses/languages/Java/lesson1')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/java/lesson2')
def java_lesson2():
    path = os.path.join(app.template_folder, 'courses/languages/Java/lesson2')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/java/lesson3')
def java_lesson3():
    path = os.path.join(app.template_folder, 'courses/languages/Java/lesson3')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/java/lesson4')
def java_lesson4():
    path = os.path.join(app.template_folder, 'courses/languages/Java/lesson4')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/java/lesson5')
def java_lesson5():
    path = os.path.join(app.template_folder, 'courses/languages/Java/lesson5')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/java/lesson6')
def java_lesson6():
    path = os.path.join(app.template_folder, 'courses/languages/Java/lesson6')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/java/lesson7')
def java_lesson7():
    path = os.path.join(app.template_folder, 'courses/languages/Java/lesson7')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/java/lesson8')
def java_lesson8():
    path = os.path.join(app.template_folder, 'courses/languages/Java/lesson8')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/java/lesson9')
def java_lesson9():
    path = os.path.join(app.template_folder, 'courses/languages/Java/lesson9')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/java/lesson10')
def java_lesson10():
    path = os.path.join(app.template_folder, 'courses/languages/Java/lesson10')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/java/lesson11')
def java_lesson11():
    path = os.path.join(app.template_folder, 'courses/languages/Java/lesson11')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/java/lesson12')
def java_lesson12():
    path = os.path.join(app.template_folder, 'courses/languages/Java/lesson12')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/java/lesson13')
def java_lesson13():
    path = os.path.join(app.template_folder, 'courses/languages/Java/lesson13')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/java/lesson14')
def java_lesson14():
    path = os.path.join(app.template_folder, 'courses/languages/Java/lesson14')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/java/lesson15')
def java_lesson15():
    path = os.path.join(app.template_folder, 'courses/languages/Java/lesson15')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/java/lesson16')
def java_lesson16():
    path = os.path.join(app.template_folder, 'courses/languages/Java/lesson16')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/java/lesson17')
def java_lesson17():
    path = os.path.join(app.template_folder, 'courses/languages/Java/lesson17')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/java/lesson18')
def java_lesson18():
    path = os.path.join(app.template_folder, 'courses/languages/Java/lesson18')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/java/lesson19')
def java_lesson19():
    path = os.path.join(app.template_folder, 'courses/languages/Java/lesson19')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/java/lesson20')
def java_lesson20():
    path = os.path.join(app.template_folder, 'courses/languages/Java/lesson20')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/java/lesson21')
def java_lesson21():
    path = os.path.join(app.template_folder, 'courses/languages/Java/lesson21')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/java/lesson22')
def java_lesson22():
    path = os.path.join(app.template_folder, 'courses/languages/Java/lesson22')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/java/lesson23')
def java_lesson23():
    path = os.path.join(app.template_folder, 'courses/languages/Java/lesson23')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/java/lesson24')
def java_lesson24():
    path = os.path.join(app.template_folder, 'courses/languages/Java/lesson24')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/java/lesson25')
def java_lesson25():
    path = os.path.join(app.template_folder, 'courses/languages/Java/lesson25')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/java/final-exam')
def java_final_exam():
    path = os.path.join(app.template_folder, 'courses/languages/Java/Final exam')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/java/certificate')
def java_certificate():
    path = os.path.join(app.template_folder, 'courses/languages/Java/certificate')
    return send_file(path, mimetype='text/html')

# ─── C ────────────────────────────────────────────
@app.route('/courses/languages/c')
def c_course():
    path = os.path.join(app.template_folder, 'courses/languages/C/index.html')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/c/lesson1')
def c_lesson1():
    path = os.path.join(app.template_folder, 'courses/languages/C/lesson1')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/c/lesson2')
def c_lesson2():
    path = os.path.join(app.template_folder, 'courses/languages/C/lesson2')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/c/lesson3')
def c_lesson3():
    path = os.path.join(app.template_folder, 'courses/languages/C/lesson3')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/c/lesson4')
def c_lesson4():
    path = os.path.join(app.template_folder, 'courses/languages/C/lesson4')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/c/lesson5')
def c_lesson5():
    path = os.path.join(app.template_folder, 'courses/languages/C/lesson5')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/c/lesson6')
def c_lesson6():
    path = os.path.join(app.template_folder, 'courses/languages/C/lesson6')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/c/lesson7')
def c_lesson7():
    path = os.path.join(app.template_folder, 'courses/languages/C/lesson7')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/c/lesson8')
def c_lesson8():
    path = os.path.join(app.template_folder, 'courses/languages/C/lesson8')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/c/lesson9')
def c_lesson9():
    path = os.path.join(app.template_folder, 'courses/languages/C/lesson9')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/c/lesson10')
def c_lesson10():
    path = os.path.join(app.template_folder, 'courses/languages/C/lesson10')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/c/lesson11')
def c_lesson11():
    path = os.path.join(app.template_folder, 'courses/languages/C/lesson11')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/c/lesson12')
def c_lesson12():
    path = os.path.join(app.template_folder, 'courses/languages/C/lesson12')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/c/lesson13')
def c_lesson13():
    path = os.path.join(app.template_folder, 'courses/languages/C/lesson13')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/c/lesson14')
def c_lesson14():
    path = os.path.join(app.template_folder, 'courses/languages/C/lesson14')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/c/lesson15')
def c_lesson15():
    path = os.path.join(app.template_folder, 'courses/languages/C/lesson15')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/c/lesson16')
def c_lesson16():
    path = os.path.join(app.template_folder, 'courses/languages/C/lesson16')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/c/lesson17')
def c_lesson17():
    path = os.path.join(app.template_folder, 'courses/languages/C/lesson17')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/c/lesson18')
def c_lesson18():
    path = os.path.join(app.template_folder, 'courses/languages/C/lesson18')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/c/lesson19')
def c_lesson19():
    path = os.path.join(app.template_folder, 'courses/languages/C/lesson19')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/c/lesson20')
def c_lesson20():
    path = os.path.join(app.template_folder, 'courses/languages/C/lesson20')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/c/project1')
def c_project1():
    path = os.path.join(app.template_folder, 'courses/languages/C/project1')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/c/project2')
def c_project2():
    path = os.path.join(app.template_folder, 'courses/languages/C/project2')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/c/project3')
def c_project3():
    path = os.path.join(app.template_folder, 'courses/languages/C/project3')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/c/project4')
def c_project4():
    path = os.path.join(app.template_folder, 'courses/languages/C/project4')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/c/project5')
def c_project5():
    path = os.path.join(app.template_folder, 'courses/languages/C/project5')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/c/final-exam')
def c_final_exam():
    path = os.path.join(app.template_folder, 'courses/languages/C/final exam')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/c/certificate')
def c_certificate():
    path = os.path.join(app.template_folder, 'courses/languages/C/certificate')
    return send_file(path, mimetype='text/html')

# ─── C++ ──────────────────────────────────────────
@app.route('/courses/languages/cpp')
def cpp_course():
    path = os.path.join(app.template_folder, 'courses/languages/cpp/index.html')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/cpp/lesson1')
def cpp_lesson1():
    path = os.path.join(app.template_folder, 'courses/languages/cpp/lesson1')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/cpp/lesson2')
def cpp_lesson2():
    path = os.path.join(app.template_folder, 'courses/languages/cpp/lesson2')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/cpp/lesson3')
def cpp_lesson3():
    path = os.path.join(app.template_folder, 'courses/languages/cpp/lesson3')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/cpp/lesson4')
def cpp_lesson4():
    path = os.path.join(app.template_folder, 'courses/languages/cpp/lesson4')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/cpp/lesson5')
def cpp_lesson5():
    path = os.path.join(app.template_folder, 'courses/languages/cpp/lesson5')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/cpp/lesson6')
def cpp_lesson6():
    path = os.path.join(app.template_folder, 'courses/languages/cpp/lesson6')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/cpp/lesson7')
def cpp_lesson7():
    path = os.path.join(app.template_folder, 'courses/languages/cpp/lesson7')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/cpp/lesson8')
def cpp_lesson8():
    path = os.path.join(app.template_folder, 'courses/languages/cpp/lesson8')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/cpp/lesson9')
def cpp_lesson9():
    path = os.path.join(app.template_folder, 'courses/languages/cpp/lesson9')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/cpp/lesson10')
def cpp_lesson10():
    path = os.path.join(app.template_folder, 'courses/languages/cpp/lesson10')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/cpp/lesson11')
def cpp_lesson11():
    path = os.path.join(app.template_folder, 'courses/languages/cpp/lesson11')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/cpp/lesson12')
def cpp_lesson12():
    path = os.path.join(app.template_folder, 'courses/languages/cpp/lesson12')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/cpp/lesson13')
def cpp_lesson13():
    path = os.path.join(app.template_folder, 'courses/languages/cpp/lesson13')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/cpp/lesson14')
def cpp_lesson14():
    path = os.path.join(app.template_folder, 'courses/languages/cpp/lesson14')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/cpp/lesson15')
def cpp_lesson15():
    path = os.path.join(app.template_folder, 'courses/languages/cpp/lesson15')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/cpp/lesson16')
def cpp_lesson16():
    path = os.path.join(app.template_folder, 'courses/languages/cpp/lesson16')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/cpp/lesson17')
def cpp_lesson17():
    path = os.path.join(app.template_folder, 'courses/languages/cpp/lesson17')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/cpp/lesson18')
def cpp_lesson18():
    path = os.path.join(app.template_folder, 'courses/languages/cpp/lesson18')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/cpp/lesson19')
def cpp_lesson19():
    path = os.path.join(app.template_folder, 'courses/languages/cpp/lesson19')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/cpp/lesson20')
def cpp_lesson20():
    path = os.path.join(app.template_folder, 'courses/languages/cpp/lesson20')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/cpp/lesson21')
def cpp_lesson21():
    path = os.path.join(app.template_folder, 'courses/languages/cpp/lesson21')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/cpp/lesson22')
def cpp_lesson22():
    path = os.path.join(app.template_folder, 'courses/languages/cpp/lesson22')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/cpp/lesson23')
def cpp_lesson23():
    path = os.path.join(app.template_folder, 'courses/languages/cpp/lesson23')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/cpp/lesson24')
def cpp_lesson24():
    path = os.path.join(app.template_folder, 'courses/languages/cpp/lesson24')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/cpp/lesson25')
def cpp_lesson25():
    path = os.path.join(app.template_folder, 'courses/languages/cpp/lesson25')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/cpp/lesson26')
def cpp_lesson26():
    path = os.path.join(app.template_folder, 'courses/languages/cpp/lesson26')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/cpp/lesson27')
def cpp_lesson27():
    path = os.path.join(app.template_folder, 'courses/languages/cpp/lesson27')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/cpp/lesson28')
def cpp_lesson28():
    path = os.path.join(app.template_folder, 'courses/languages/cpp/lesson28')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/cpp/lesson29')
def cpp_lesson29():
    path = os.path.join(app.template_folder, 'courses/languages/cpp/lesson29')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/cpp/lesson30')
def cpp_lesson30():
    path = os.path.join(app.template_folder, 'courses/languages/cpp/lesson30')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/cpp/lesson31')
def cpp_lesson31():
    path = os.path.join(app.template_folder, 'courses/languages/cpp/lesson31')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/cpp/lesson32')
def cpp_lesson32():
    path = os.path.join(app.template_folder, 'courses/languages/cpp/lesson32')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/cpp/lesson33')
def cpp_lesson33():
    path = os.path.join(app.template_folder, 'courses/languages/cpp/lesson33')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/cpp/lesson34')
def cpp_lesson34():
    path = os.path.join(app.template_folder, 'courses/languages/cpp/lesson34')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/cpp/lesson35')
def cpp_lesson35():
    path = os.path.join(app.template_folder, 'courses/languages/cpp/lesson35')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/cpp/lesson36')
def cpp_lesson36():
    path = os.path.join(app.template_folder, 'courses/languages/cpp/lesson36')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/cpp/lesson37')
def cpp_lesson37():
    path = os.path.join(app.template_folder, 'courses/languages/cpp/lesson37')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/cpp/lesson38')
def cpp_lesson38():
    path = os.path.join(app.template_folder, 'courses/languages/cpp/lesson38')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/cpp/lesson39')
def cpp_lesson39():
    path = os.path.join(app.template_folder, 'courses/languages/cpp/lesson39')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/cpp/lesson40')
def cpp_lesson40():
    path = os.path.join(app.template_folder, 'courses/languages/cpp/lesson40')
    return send_file(path, mimetype='text/html')

# ─── C++ פרויקטים ─────────────────────────────────
@app.route('/courses/languages/cpp/level1-project')
def cpp_level1_project():
    path = os.path.join(app.template_folder, 'courses/languages/cpp/level1 project')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/cpp/level2-project')
def cpp_level2_project():
    path = os.path.join(app.template_folder, 'courses/languages/cpp/level2 project')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/cpp/level3-project')
def cpp_level3_project():
    path = os.path.join(app.template_folder, 'courses/languages/cpp/level3 project')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/cpp/level4-project')
def cpp_level4_project():
    path = os.path.join(app.template_folder, 'courses/languages/cpp/level4 project')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/cpp/level5-project')
def cpp_level5_project():
    path = os.path.join(app.template_folder, 'courses/languages/cpp/level5 project')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/cpp/level6-project')
def cpp_level6_project():
    path = os.path.join(app.template_folder, 'courses/languages/cpp/level6 project')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/cpp/level7-project')
def cpp_level7_project():
    path = os.path.join(app.template_folder, 'courses/languages/cpp/level7 project')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/cpp/level8-project')
def cpp_level8_project():
    path = os.path.join(app.template_folder, 'courses/languages/cpp/level8 project')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/cpp/level9-project')
def cpp_level9_project():
    path = os.path.join(app.template_folder, 'courses/languages/cpp/level9 project')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/cpp/level10-project')
def cpp_level10_project():
    path = os.path.join(app.template_folder, 'courses/languages/cpp/level10 project')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/cpp/level10-finalexam')
def cpp_level10_finalexam():
    path = os.path.join(app.template_folder, 'courses/languages/cpp/level10 finalexam')
    return send_file(path, mimetype='text/html')

@app.route('/courses/languages/cpp/level10-certificate')
def cpp_level10_certificate():
    path = os.path.join(app.template_folder, 'courses/languages/cpp/level10 certificate')
    return send_file(path, mimetype='text/html')

if __name__ == '__main__':
    app.run(debug=False)

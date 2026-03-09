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

@app.route('/learn')
def learn():
    return render_template('learn.html')

@app.route('/Profile')
@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/vision')
def vision():
    return render_template('vision.html')

if __name__ == '__main__':
    app.run(debug=False)

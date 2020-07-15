# import Flask class from flask  package
from flask import Flask, render_template
# create an instance of Flask class by providing the application module as parameter
app = Flask(__name__) 

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')
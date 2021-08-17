from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.survey import Survey


@app.route('/')
def home():
    return render_template("index.html")

# @app.route('/application',methods=['POST'])
# def process():
#     session['name'] = request.form['name']
#     session['location'] = request.form['location']
#     session['language'] = request.form['language']
#     session['comments'] = request.form['comments']
#     return redirect('/result')

@app.route('/survey/create', methods=['POST'])
def create_survey():
    if Survey.is_valid(request.form):
        Survey.save_survey(request.form)
        return redirect('/result')
    return redirect('/')


@app.route('/result')
def success():
    return render_template('result.html', survey = Survey.get_survey())
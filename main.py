from flask import Flask, render_template, request,jsonify
from recommender import get_recommendations
import os

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('questions.html')

@app.route('/questions', methods=['GET','POST'])
def reco_system():

    if request.method == 'GET':
        return jsonify({"response":"Send a POST request with lessonId"})
    else:
        data = request.get_json()
        lessonId = data['lessonId']
        questions = get_recommendations(lessonId)
        return questions

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST' or request.method == 'GET':
        lessonId = request.form['lessonId']
        questions = get_recommendations(lessonId)
        return questions
    else:
        return render_template('questions.html', message='Please enter required fields')
    
if __name__ == '__main__':
    app.run()
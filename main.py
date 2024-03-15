from flask import Flask, render_template, request,jsonify
from flask_cors import CORS
from recommender import get_recommendations

app = Flask(__name__)
CORS(app, resources={r"*":{"origins":"*"}})

# @app.route('/')
# def main():
#     return render_template('questions.html')

@app.route('/', methods=['GET','POST'])
def reco_system():

    if request.method == 'GET':
        return jsonify({"response":"Send a POST request with lessonId"})
    else:
        data = request.get_json()
        lessonId = data['lessonId']
        questions = get_recommendations(lessonId)
        return questions

# @app.route('/submit', methods=['POST', 'GET'])
# def submit():
#     if request.method == 'POST' or request.method == 'GET':
#         lessonId = request.form['lessonId']
#         questions = get_recommendations(lessonId)
#         return questions
#     else:
#         return render_template('questions.html', message='Please enter required fields')
    
if __name__ == '__main__':
    app.run()
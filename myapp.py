# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request, render_template_string, redirect, url_for
from prediction import openai_stock_prediction 
import requests
from utils import get_true_answer

class MyApp:
    def __init__(self, db):
        self.app = Flask(__name__)
        self.osp = openai_stock_prediction()
        self.setup_routes()
        self.feedback_checker = 'True'
        self.input_query = ''
        self.input_anwer = ''
        self.db = db

    def setup_routes(self):
        @self.app.route('/')
        def home():
            return render_template_string(self.form_template)

        @self.app.route('/submit', methods=['POST'])
        def submit_text():
            text = request.form['textinput']

            response = requests.post('http://localhost:8000/prediction/', json={'text': text})
            answer = response.json()['text'].split()[-1]
            self.input_query = self.db.form_checker(text)
            self.input_anwer = answer
            text = self.input_query+': '+self.input_anwer

            # 결과 페이지에 텍스트를 보여주고, 사용자가 직접 리디렉션할 수 있는 버튼 제공
            return render_template_string(self.result_template, text=text)
        
        @self.app.route('/feedback', methods=['POST'])
        def handle_feedback():
            feedback = request.form['feedback']  # 'true' 또는 'false' 값을 받습니다.

            query_to_be_saved = self.input_query+ ': ' + get_true_answer(self.input_anwer, True)
            print(query_to_be_saved)
            if feedback == 'true':
                self.db.insert_sentence(query_to_be_saved, )
            elif feedback == 'false':
                self.db.insert_sentence(query_to_be_saved, )
            return redirect(url_for('home'))
    
    def add_prompt(self, prompt):
        self.prompts.append(prompt)
        
    def run(self, *args, **kwargs):
        self.app.run(*args, **kwargs)

    @property
    def form_template(self):
        return """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Input Form</title>
        </head>
        <body>
            <h2>Text Input Form</h2>
                <form method="post" action="/submit">
                <textarea name="textinput" placeholder="여기에 입력하세요" rows="4" cols="50"></textarea>
                <input type="submit" />
            </form>
        </body>
        </html>
        """
    @property
    def result_template(self):
        return """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Submission Result</title>
        </head>
        <body>
            <h2>Submission Result</h2>
            <p>Received text: {{ text }}</p>
            <form action="/feedback" method="post">
                <input type="hidden" name="text" value="{{ text }}">
                <button type="submit" name="feedback" value="true">true</button>
                <button type="submit" name="feedback" value="false">false</button>
                <button type="submit" name="feedback" value="none">don't know</button>
            </form>
        </body>
        </html>
        """
    

if __name__ == "__main__":
  print('myapp')
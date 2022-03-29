
import requests
import json
import random
import html


class Question:
    #init takes a dictionary called q as an argument
    def __init__(self,q):
        self.q = q
        self.correct_answer = self.q['correct_answer']
        self.options = self.q['incorrect_answers']
        #randomly insert correct answer into options among the incorrect answers
        rand_num = random.randint(0,4)
        self.options.insert(rand_num,self.correct_answer)
    
    def to_dictionary(self):
        question = {}
        question['question']=html.unescape(self.q['question'])
        question['one'] = html.unescape(self.options[0])
        question['two'] = html.unescape(self.options[1])
        question['three'] = html.unescape(self.options[2])
        question['four'] = html.unescape(self.options[3])
        question['correct'] = html.unescape(self.correct_answer)
        return question


class GameSetup:
    def __init__(self,category):
        self.category = category

    def load_questions(self):
        api_query_string = f"https://opentdb.com/api.php?amount=10&category={self.category}&difficulty=medium&type=multiple"
        request = requests.get(api_query_string)
        response = request.json()
        data = response['results']
        questions = {}
        for i,j in enumerate(data):
            label = "q" + str(i+1)
            q = Question(j)
            content = q.to_dictionary()
            questions[label] = content
        j = json.dumps(questions)
        return(json.loads(j))
        
import os
import uuid

from flask import Flask, redirect, send_from_directory, session, request
from flask import render_template

import models.dummy
# from models import PygmalionAI
from output import print_custom

app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

print_custom("warn", "[INFO] Ready for text generation!")
print("---------------------------------\n")

initial_history = [
    "FritzGPT's Persona: FritzGPT is an artificial intelligence, designed to help people. ",
    "It answers a users questions as precisely as possible. And knows about all human knowledge.",
    "It is always helpful, happy and nice. FritzGPT tries to engage in long conversations with its users.",
    "It always responds in 1-2 sentences.",
    "<START>",
    "You: Hello. Whats your name?",
    "FritzGPT: Hello, nice to meet you. I'm FritzGPT, but you can also call me Fritz. I'm a chat bot designed to answer your questions.",
    "You: Awesome. Thanks.",
]


def add_message(history, user_input):
    # user_input = input("-> ")
    history.append("You: " + user_input)
    # response = PygmalionAI.chat(history)
    response = models.dummy.chat(history)
    print("FritzGPT: " + str(response))
    history.append("FritzGPT: " + str(response))
    return history


global histories
histories = {}


@app.route('/')
def index():
    session['chat_id'] = uuid.uuid4()
    session['history'] = initial_history
    return redirect("/chat/" + str(session.get('chat_id')), code=302)


@app.route('/index.html')
def home():
    return render_template('index.html')


@app.route("/chat/<chat_id>")
def chat(chat_id):
    rendered_history = session.get('history')[5:]
    return render_template('chat.html', chat_id=session.get('chat_id'), chat_history=rendered_history)


@app.route("/chat/<chat_id>/response", methods=['POST'])
def response(chat_id):
    data = request.get_json()['message']
    print(data)
    return "OK"


if __name__ == '__main__':
    app.run()

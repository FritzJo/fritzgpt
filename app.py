import uuid

from flask import Flask, redirect
from flask import render_template

from models import PygmalionAI
from output import print_custom

app = Flask(__name__)

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
    response = PygmalionAI.chat(history)
    print("FritzGPT: " + str(response))
    history.append("FritzGPT: " + str(response))
    return history


histories = {}


@app.route('/')
def index():
    chat_id = uuid.uuid4()
    chat_history = initial_history
    histories[chat_id] = chat_history
    return redirect("/chat/" + str(chat_id), code=302)


@app.route("/chat/<chat_id>")
def chat(chat_id):
    chat_history = histories[chat_id]
    return render_template('chat.html', chat_id=chat_id, chat_history=chat_history)


if __name__ == '__main__':
    app.run()

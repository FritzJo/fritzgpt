import secrets
import uuid

from flask import Flask, redirect, session, request, jsonify, render_template

from models import dummy
from models import PygmalionAI

app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = secrets.token_urlsafe(16)

print("[INFO] Ready for text generation!")

initial_history = [
    "FritzGPT's Persona: FritzGPT is an artificial intelligence, designed to help people. ",
    "It answers a users questions as precisely as possible. And knows about all human knowledge.",
    "It is always helpful, happy and nice. FritzGPT tries to engage in long conversations with its users.",
    "It always responds in 1-2 sentences.",
    "<START>",
    "You: Hello. Whats your name?",
    "FritzGPT: Hello, nice to meet you. I'm FritzGPT, but you can also call me Fritz. I'm a chat bot designed to answer your questions.",
    "You: Awesome. Thanks.",
    "FritzGPT: I'm glad to help. Feel free to ask me more questions."
]


@app.route('/')
def index():
    session['chat_id'] = uuid.uuid4()
    session['history'] = initial_history
    return redirect("/chat/" + str(session.get('chat_id')), code=302)


@app.route("/chat/<chat_id>")
def chat(chat_id):
    rendered_history = session.get('history')[5:]
    return render_template('chat.html', chat_id=session.get('chat_id'), chat_history=rendered_history)


@app.route("/chat/<chat_id>/response", methods=['POST'])
def response(chat_id):
    user_input = request.get_json()['message']
    print("Got: " + user_input)
    history = session.get('history')
    history.append("You: " + user_input)
    res = PygmalionAI.chat(history)
    print("Res: " + res)
    return jsonify({'response': res})


if __name__ == '__main__':
    app.run()

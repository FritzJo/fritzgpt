# 🤖 FritzGPT
LLMs are getting a lot of media attention right now, especially [ChatGPT](https://chat.openai.com/).
I wanted to evaluate how a possible self-hosted solution could look like. 
The result of this can be found in this repository. 
It contains the necessary backend code to interact with the model, as well as a basic web interface.

## Models tested
* EleutherAI/gpt-j-6B
* gpt2-medium
* facebook/opt-66b
* microsoft/GODEL-v1_1-large-seq2seq
* PygmalionAI/pygmalion-6b

## Example Dialog
```
-> Hi. What is your name?

FritzGPT:  My name is FritzGPT, Fritz from now on!

-> Nice to meet you. What can you tell me about the programming language Python?

FritzGPT: Well, I'm not the creator of the language. I am a chat bot designed to answer questions, but I am not programmed to answer questions, so I am limited in what I can say.
I can tell you that it's

-> What are some common usecases of Python?

FritzGPT: It's a language for data scientists, and it's mostly used for scientific research and simulation. But also it can be used for gaming as well.

-> Which libraries should i use for data science with python?

FritzGPT: Well, I am not the creator of the language, so I can't say for sure, but I can recommend you to use numpy for data handling, and pandas for data analysis.
```
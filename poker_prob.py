import logging
import os

from flask import Flask
from flask_ask import Ask, request, session, question, statement


app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)


@ask.launch
def launch():
    speech_text = 'Welcome to Poker Probabilities. List two cards and I will provide your heads-up win percentage.'
    return question(speech_text).reprompt(speech_text).simple_card('PokerProbabilities', speech_text)


@ask.intent('HelloWorldIntent')
def hello_world():
    speech_text = 'Welcome to poker probabilities.'
    return statement(speech_text).simple_card('PokerProbabilities', speech_text)


@ask.intent('AMAZON.HelpIntent')
def help():
    speech_text = 'List two cards and I will provide your heads-up win percentage.'
    return question(speech_text).reprompt(speech_text).simple_card('PokerProbabilities', speech_text)


@ask.session_ended
def session_ended():
    return "{}", 200


if __name__ == '__main__':
    if 'ASK_VERIFY_REQUESTS' in os.environ:
        verify = str(os.environ.get('ASK_VERIFY_REQUESTS', '')).lower()
        if verify == 'false':
            app.config['ASK_VERIFY_REQUESTS'] = False
    app.run(debug=True)
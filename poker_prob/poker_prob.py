import logging

import requests

from flask import Flask
from flask_ask import Ask, statement

app = Flask(__name__)
ask = Ask(app, '/')
logger = logging.getLogger()

@ask.launch
def launch():
    return poker()

@ask.intent("PokerIntent")
def poker():
    speech = "The winning probability of your cards is 99%"

    return statement(speech)
import logging

import requests

from flask import Flask
from flask_ask import Ask, statement

app = Flask(__name__)
ask = Ask(app, '/')
logger = logging.getLogger()

@ask.launch
def launch():
    return poker1()

@ask.intent("Poker1Intent")
def poker1():
    speech = "The winning probability of your cards is 99%"

    return statement(speech)
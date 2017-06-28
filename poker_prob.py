import logging
import os

from flask import Flask, json, render_template
from flask_ask import Ask, request, session, question, statement


app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)


probs = {
    'AA': 84.97,
    'KK': 82.10,
    'QQ': 79.63,
    'JJ': 77.16,
    'TT': 74.66,
    '99': 71.69,
    '88': 68.72,
    'KAs': 65.28,
    'QAs': 64.41,
    '77': 65.72,
    'JAs': 63.55,
    'KA': 63.49,
    'TAs': 62.66,
    'QA': 62.57,
    'JA': 61.63,
    'QKs': 61.58,
    '9As': 60.68,
    'TA': 60.70,
    'JKs': 60.69,
    '66': 62.58,
    '8As': 59.72,
    'TKs': 59.82,
    '7As': 58.61,
    'QK': 59.58,
    '9A': 58.60,
    '5As': 57.31,
    'JK': 58.64,
    'JQs': 58.43,
    '6As': 57.26,
    '9Ks': 57.89,
    '8A': 57.54,
    'TK': 57.72,
    'TQs': 57.56,
    '4As': 56.38,
    '55': 59.65,
    '7A': 56.36,
    '3As': 55.60,
    '8Ks': 56.08,
    '5A': 54.94,
    'JQ': 56.25,
    '6A': 54.91,
    '2As': 54.84,
    '7Ks': 55.13,
    '9K': 55.64,
    '9Qs': 55.62,
    'TJs': 55.67,
    'TQ': 55.31,
    '4A': 53.95,
    '6Ks': 53.98,
    '3A': 53.08,
    '5Ks': 53.15,
    '8Qs': 53.85,
    '8K': 53.68,
    '44': 56.26,
    '9Js': 53.65,
    '9Q': 53.25,
    '7K': 52.68,
    '2A': 52.24,
    'TJ': 53.34,
    '4Ks': 52.20,
    '7Qs': 51.96,
    '3Ks': 51.39,
    '6K': 51.44,
    '9Ts': 52.05,
    '8Js': 51.87,
    '6Qs': 51.02,
    '8Q': 51.34,
    '5K': 50.54,
    '2Ks': 50.58,
    '9J': 51.16,
    '5Qs': 50.18,
    '8Ts': 50.21,
    '4K': 49.51,
    '7Js': 50.01,
    '33': 52.84,
    '4Qs': 49.23,
    '7Q': 49.32,
    '9T': 49.47,
    '3K': 48.61,
    '8J': 49.25,
    '3Qs': 48.41,
    '89s': 48.63,
    '6Q': 48.29,
    '7Ts': 48.35,
    '6Js': 48.03,
    '2K': 47.73,
    '5Q': 47.39,
    '5Js': 47.41,
    '2Qs': 47.56,
    '8T': 47.49,
    '7J': 47.28,
    '79s': 46.78,
    '4Js': 46.45,
    '4Q': 46.36,
    '6Ts': 46.39,
    '22': 49.41,
    '3Js': 45.62,
    '78s': 45.57,
    '3Q': 45.46,
    '89': 45.85,
    '7T': 45.51,
    '6J': 45.16,
    '69s': 44.85,
    '5Ts': 44.65,
    '2Js': 44.79,
    '5J': 44.47,
    '2Q': 44.56,
    '4Ts': 43.91,
    '68s': 43.58,
    '79': 43.87,
    '4J': 43.43,
    '6T': 43.42,
    '59s': 43.14,
    '3Ts': 43.08,
    '67s': 42.60,
    '78': 42.58,
    '3J': 42.54,
    '58s': 41.87,
    '2Ts': 42.24,
    '69': 41.78,
    '5T': 41.54,
    '2J': 41.65,
    '57s': 40.93,
    '49s': 41.22,
    '4T': 40.75,
    '56s': 40.16,
    '68': 40.44,
    '39s': 40.61,
    '48s': 39.98,
    '59': 39.94,
    '3T': 39.84,
    '67': 39.39,
    '29s': 39.78,
    '47s': 39.06,
    '45s': 38.54,
    '58': 38.63,
    '46s': 38.30,
    '2T': 38.94,
    '38s': 38.16,
    '57': 37.63,
    '49': 37.89,
    '28s': 37.58,
    '37s': 37.25,
    '56': 36.83,
    '35s': 36.76,
    '39': 37.23,
    '36s': 36.51,
    '48': 36.60,
    '29': 36.34,
    '34s': 35.74,
    '47': 35.61,
    '45': 35.08,
    '46': 34.82,
    '27s': 35.40,
    '25s': 34.93,
    '26s': 34.68,
    '38': 34.64,
    '24s': 33.95,
    '28': 33.99,
    '37': 33.67,
    '35': 33.16,
    '36': 32.90,
    '23s': 33.12,
    '34': 32.08,
    '27': 31.68,
    '25': 31.21,
    '26': 30.91,
    '24': 30.14,
    '23': 29.29
}


card_abbrvs = {
    'ace': 'A',
    'king': 'K',
    'queen': 'Q',
    'jack': 'J',
    'ten': 'T',
    'nine': '9',
    'eight': '8',
    'seven': '7',
    'six': '6',
    'five': '5',
    'four': '4',
    'three': '3',
    'two': '2',
    # apparently numbers come in as numbers...
    '10': 'T',
    '9': '9',
    '8': '8',
    '7': '7',
    '6': '6',
    '5': '5',
    '4': '4',
    '3': '3',
    '2': '2',
    10: 'T',
    9: '9',
    8: '8',
    7: '7',
    6: '6',
    5: '5',
    4: '4',
    3: '3',
    2: '2',
}


@ask.launch
def launch():
    speech_text = 'Welcome to Poker Probabilities. List two cards and I will provide your heads-up win percentage.'
    return question(speech_text).reprompt(speech_text).simple_card('Poker Probabilities', speech_text)


@ask.intent('HelloWorldIntent')
def hello_world():
    speech_text = 'Welcome to poker probabilities.'
    return statement(speech_text).simple_card('Poker Probabilities', speech_text)

@ask.intent('PokerIntent')
def poker(CardA, CardB):
    #speech_text = render_template('win_reposne', carda=CardA, cardb=CardB)

    return poker_prob(CardA, CardB, "")

@ask.intent('PokerSuitedIntent')
def poker(CardA, CardB):

    # Check for potential fail case of asking for suited for the same cards
    if (CardA == CardB):
        return poker_prob(CardA, CardB, "")

    return poker_prob(CardA, CardB, "s")



def poker_prob(CardA, CardB, is_suited):
    CardA = CardA.strip().lower()
    CardB = CardB.strip().lower()

    ca = ""
    if (CardA) in card_abbrvs:
        ca = card_abbrvs[CardA]
    else:
        speech_text = "I'm sorry, but I don't recognize the card '%s'" % CardA
        return statement(speech_text).simple_card('Poker Probabilities', speech_text)

    cb = ""
    if (CardB) in card_abbrvs:
        cb = card_abbrvs[CardB]
    else:
        speech_text = "I'm sorry, but I don't recognize the card '%s'" % CardB
        return statement(speech_text).simple_card('Poker Probabilities', speech_text)


    abbrv = ca+cb+is_suited
    if not abbrv in probs:
        abbrv = cb+ca+is_suited
        if not abbrv in probs:
            speech_text = "I'm sorry, an unexpected error occurred looking up %s (%s) and %s (%s)" % (CardA, ca, CardB, cb)
            return statement(speech_text).simple_card('Poker Probabilities', speech_text)

    suit_status = "offsuit"
    if is_suited == "s":
        suit_status = "suited"

    #speech_text = render_template('win_reposne', carda=CardA, cardb=CardB)
    speech_text = "The win percentage with %s and %s %s is %s" % (CardA, CardB, suit_status, probs[abbrv])
    return statement(speech_text).simple_card('Poker Probabilities', speech_text)

@ask.intent('AMAZON.HelpIntent')
def help():
    speech_text = render_template('help')
    return question(speech_text).reprompt(speech_text).simple_card('Poker Probabilities', speech_text)


@ask.intent('AMAZON.StopIntent')
def stop():
    bye_text = render_template('bye')
    return statement(bye_text)


@ask.intent('AMAZON.CancelIntent')
def cancel():
    bye_text = render_template('bye')
    return statement(bye_text)


@ask.session_ended
def session_ended():
    return "{}", 200


if __name__ == '__main__':
    if 'ASK_VERIFY_REQUESTS' in os.environ:
        verify = str(os.environ.get('ASK_VERIFY_REQUESTS', '')).lower()
        if verify == 'false':
            app.config['ASK_VERIFY_REQUESTS'] = False
    app.run(debug=True)
from flask import Flask
import random

from flask.helpers import flash
import random

app = Flask(__name__)

randnumber = random.randint(1,10)

correct = '<h1>You are Correct!</h1><p>Please refresh to play again!</p> <img src="https://media.giphy.com/media/PS7d4tm1Hq6Sk/giphy.gif">'

low = '<h1>Too low!</h1><p>Please guess again!</p> <img src="https://media.giphy.com/media/3OhXBaoR1tVPW/giphy.gif">'

high = '<h1>Too high!</h1><p>Please guess again!</p> <img src="https://media.giphy.com/media/zu8DrkFiuz8JO/giphy.gif">'

@app.route('/')
def home():
    return "<p>Please add a number after the URL between 1 and 10</p>"


@app.route('/<number>')
def isCorrect(number):
    if(int(number) == randnumber):
        return correct
    elif(int(number) > randnumber):
        return high
    else:
        return low

if __name__ == "__main__":
    app.run(debug=True)
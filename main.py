from flask import Flask
import random

from flask.helpers import flash

app = Flask(__name__)

randnumber = random.randint(1,10)

correct = '<h1>You are Correct!</h1><p>Please refresh to play again!</p> <img src="https://media.giphy.com/media/PS7d4tm1Hq6Sk/giphy.gif">'

low = '<h1>Too low!</h1><p>Please guess again!</p> <img src="https://media.giphy.com/media/3OhXBaoR1tVPW/giphy.gif">'

high = '<h1>Too high!</h1><p>Please guess again!</p> <img src="https://media.giphy.com/media/9DlCEg3G79DY0jFlMo/giphy.gif">'

@app.route(/<number>)
def isCorrect(number):
    if(number == randnumber):
        return correct
    elif(number > randnumber):
        return high
    else:
        return low

if __name__ == "__main__":
    app.run(debug=True)
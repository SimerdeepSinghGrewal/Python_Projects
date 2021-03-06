from flask import Flask
from random import randint

app = Flask(__name__)


@app.route('/')
def main():
    return "<h1>Guess a number between 0 and 9</h1><img src=https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif>"


number = randint(0, 9)


@app.route('/<numb>')
def num(numb):
    numb = int(numb)
    if numb < number:
        return "<h1 style: color=red>Too Low</h1><img src=https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif>"
    elif numb > number:
        return "<h1 style: color=blue>Too High</h1><img src=https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif>"
    elif numb == number:
        return "<h1 style: color=green>You Found Me</h1><img src=https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif>"


if __name__ == "__main__":
    app.run(debug=True)

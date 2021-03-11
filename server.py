from flask import Flask
from random import randint


app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return f'<b>{function()}</b>'
    return wrapper


def make_emphasised(function):
    def wrapper():
        return f'<em>{function()}</em>'
    return wrapper


def make_underlined(function):
    def wrapper():
        return f'<u>{function()}</u>'
    return wrapper


def make_center(function):
    def wrapper():
        return f'<center>{function()}</center>'
    return wrapper


def make_h1(function):
    def wrapper():
        return f'<h1>{function()}</h1>'
    return wrapper


def make_h2(function):
    def wrapper():
        return f'<h2>{function()}</h2>'
    return wrapper


@app.route("/")
def home():
    return f'{heading1()}<p>' \
           f'{heading2()}<p>' \
           f'{gif()}<p>'


@make_bold
@make_center
@make_h1
def heading1():
    return f'Higher or Lower ?'


@make_bold
@make_center
@make_h2
def heading2():
    return 'Guess a number between 0 and 9'


@make_center
def gif():
    return '<img src="http://www.clipartbest.com/cliparts/xTg/6pn/xTg6pnXGc.gif">'


@app.route("/<int:choice>")
def choose(choice):
    if choice < target:
        return '<h1 style="color:blue">Too low, try again!</h1><p>' \
               '<img src="https://g3fashion.com/blog/wp-content/uploads/2015/09/7-2.gif">'
    elif choice > target:
        return '<h1 style="color:red">Too high, try again!</h1><p>' \
               '<img src="https://media1.tenor.com/images/8b5924135b1225ae9ae7156338dc03f2/tenor.gif?itemid=5803400">'
    else:
        return '<h1 style="color:green">You Win!</h1><p>' \
               '<img src="https://media.giphy.com/media/50bAIiYzs6Ipi/giphy.gif">'


# Run the server from code
if __name__ == "__main__":
    target = randint(1, 9)

    # https://flask.palletsprojects.com/en/1.1.x/quickstart/#debug-mode
    app.run(debug=True)  # Enables dynamic update when code changes


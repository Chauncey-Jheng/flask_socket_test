from flask import Flask
from flask import redirect
from flask import url_for
from flask import render_template
import click

app = Flask(__name__)       

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/hello")
def greet():
    # @app.after_request_funcs
    # def do_something():
    #     print("hhhh")
    return '<h1>Hello Flask! This is a test</h1>'

@app.route("/hi")
def hi():
    return redirect(url_for('greet'))

@app.cli.command()
def hello():
    """Just say hello"""
    click.echo("Hello, there!")

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=3100, debug=True)
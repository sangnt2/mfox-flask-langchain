from flask import Blueprint

index = Blueprint('index', __name__)

@index.route('/')
def hello_world():
    return "<p>I am Flask + Langchain</p>"
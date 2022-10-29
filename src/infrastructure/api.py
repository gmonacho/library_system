import flask
from src.infrastructure.book.routes import book_api


app = flask.Flask(__name__)

app.register_blueprint(book_api)

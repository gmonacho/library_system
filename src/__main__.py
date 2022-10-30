import flask
from logging.config import dictConfig
from src.infrastructure.book.borrowing.routes import borrowing_api
from src.infrastructure.book.routes import book_api
from src.infrastructure.orm import Base, engine

dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
            }
        },
        "handlers": {
            "wsgi": {
                "class": "logging.StreamHandler",
                "stream": "ext://flask.logging.wsgi_errors_stream",
                "formatter": "default",
            }
        },
        "root": {"level": "INFO", "handlers": ["wsgi"]},
    }
)

app = flask.Flask(__name__)

app.register_blueprint(book_api)
app.register_blueprint(borrowing_api)

Base.metadata.create_all(engine)

app.run(host="0.0.0.0", debug=True)

from flask import Flask
from app.config import Config
import psycopg2
from psycopg2.extras import RealDictCursor

db_connection = psycopg2.connect(Config.DATABASE_DNS)
db_cursor = db_connection.cursor(cursor_factory=RealDictCursor)

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    from app.index.routes import index
    from app.retrieval.routes import retrieval

    app.register_blueprint(index)
    app.register_blueprint(retrieval, url_prefix="/retrieval")

    return app
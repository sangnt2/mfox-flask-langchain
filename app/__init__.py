import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    if (not os.path.exists('./instance/site.db')):
        from app.models import Bot
        with app.app_context():
            db.create_all()
            chatgpt_bot = Bot(
                bot_id='CHATGPTBOT',
                bot_username='chat-gpt-bot',
            )
            db.session.add(chatgpt_bot)
            db.session.commit()
        print('create chatbot success')
    else:
        print('DB created')

    from app.index.routes import index
    app.register_blueprint(index)

    from app.retrieval.routes import retrieval
    app.register_blueprint(retrieval, url_prefix="/retrieval")

    from app.bot.routes import bot
    app.register_blueprint(bot, url_prefix="/bot")

    @app.route('/test')
    def test_page():
        return '<h1><I am Flaks and Langchain/h1>'

    return app

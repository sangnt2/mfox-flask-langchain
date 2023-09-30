from flask import Blueprint, request, jsonify
from app import db
from app.models import Bot

bot = Blueprint('bot', __name__)

@bot.route('/', methods=["GET"])
def get_bot():
    args = request.args
    bot = Bot.query.filter_by(**args.to_dict()).first()
    if bot is not None:
        return jsonify(bot.serialize)
    return jsonify({'status': 'No results'})

    
@bot.route('/update/<string:bot_id>', methods=["POST"])
def update_chatgptbot(bot_id):
    kb = request.form.get('knowledge_base')

    bot = Bot.query.filter_by(bot_id = bot_id).first()
    bot.knowledge_base = kb
    db.session.commit()

    return jsonify(bot.serialize)
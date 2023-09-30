from app.models import Bot

def retrieve_chatgpt_kb(bot_id='CHATGPTBOT'):
    kb = ''
    bot = Bot.query.filter_by(bot_id = bot_id).first()
    if (bot is not None):
        kb = bot.knowledge_base
    return kb
from app import db

def dump_datetime(value):
    """Deserialize datetime object into string form for JSON processing."""
    if value is None:
        return None
    return [value.strftime("%Y-%m-%d"), value.strftime("%H:%M:%S")]

class Bot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bot_id = db.Column(db.String(50), nullable=False)
    bot_username = db.Column(db.String(50), nullable=False)
    bot_language = db.Column(db.String(50), nullable=True, default='English')
    bot_personality = db.Column(db.String(50), nullable=True, default='Support')
    welcome_message = db.Column(db.String(), nullable=True)
    error_message = db.Column(db.String(), nullable=True)
    quota_reach_message = db.Column(db.String(), nullable=True)
    knowledge_base = db.Column(db.String(), nullable=True)
    active = db.Column(db.Boolean(), default=True)

    @property
    def serialize(self):
       return {
           'id' : self.id,
           'bot_id': self.bot_id,
           'bot_username': self.bot_username,
           'knowledge_base': self.knowledge_base
       }
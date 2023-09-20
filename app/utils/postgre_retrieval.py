from app import db_cursor as cursor

def kb_query():
    kb = ''
    try:
        query = "select knowledge_base from chatgpt_bot where bot_id='CHATGPTBOT'"
        cursor.execute(query)
        record = cursor.fetchone()
        return record['knowledge_base']
    except:
        return kb
    
def openai_key_query():
    query = "select value_actual from core_site_settings where config_name='chatgpt-bot.openai_api_key'"
    cursor.execute(query)
    record = cursor.fetchone()
    return record['value_actual']
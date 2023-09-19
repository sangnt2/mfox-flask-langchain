from flask import Blueprint, request, jsonify
from app.utils.langchain_kb_retrieval import kb_retrieve

retrieval = Blueprint('retrieval', __name__)

@retrieval.route('/', methods=["POST"])
def retrieve_kb():
    try:
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            data = request.get_json()
            q = data.get('q','')
        else:
            q = request.form.get('q')
        
        result = kb_retrieve(q=q)
        return jsonify(result)
    except:
        return jsonify({"Status":"Failure --- some error occured"})
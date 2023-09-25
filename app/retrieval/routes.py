from flask import Blueprint, request, jsonify
from app.utils.langchain_kb_retrieval import kb_retrieve

retrieval = Blueprint('retrieval', __name__)

@retrieval.route('/', methods=["POST"])
def retrieve_kb():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        data = request.get_json()
        q = data.get('q','')
    else:
        q = request.form.get('q')

    try:
        result = kb_retrieve(q=q)
        return jsonify({"code": 200, "data":result, "status": "ok"})
    except:
        return jsonify({"code":500, "status":"Failure --- some error occured"})
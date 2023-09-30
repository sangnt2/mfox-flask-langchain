from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema.document import Document
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.vectorstores import Chroma
from app.config import Config
from app.utils import db_retrieval

def get_embedding(type = '', model_name = ''):
    if type == 'hugginface_instruct':
        embedding = HuggingFaceInstructEmbeddings(model_name=model_name)
    else:
        embedding = OpenAIEmbeddings(openai_api_key=Config.OPENAI_KEY)
    return embedding

def kb_retrieve(q=''):
    kb = db_retrieval.retrieve_chatgpt_kb()
   
    if kb == '':
        return kb

    separators = ["\n\n", "\n"]

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=255,
        chunk_overlap=25,
        length_function=len,
        separators=separators,
        # is_separator_regex = False,
    )

    documents = text_splitter.split_documents(documents=[Document(page_content=kb)])

    embedding = get_embedding()

    vector_store = Chroma.from_documents(documents=documents, embedding=embedding)

    retrieved_docs = vector_store.similarity_search_with_relevance_scores(query=q)

    most_relevant = retrieved_docs[0][0]
    most_relevant_score = float(retrieved_docs[0][1])

    if most_relevant_score > 0.8:
        return most_relevant.page_content

    return ''

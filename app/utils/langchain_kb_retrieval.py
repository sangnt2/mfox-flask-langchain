from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema.document import Document
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from app.config import Config
from app.utils import postgre_retrieval

def kb_retrieve(q=''):
    
    kb = postgre_retrieval.kb_query()
    openai_key =postgre_retrieval.openai_key_query()
    
    if (kb == ''):
        return kb

    separators = ["\n\n", "\n"]

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 155,
        chunk_overlap  = 15,
        length_function = len,
        separators=separators,
        # is_separator_regex = False,
    )

    documents = text_splitter.split_documents(documents=[Document(page_content=kb)])
    
    embedding = OpenAIEmbeddings(openai_api_key=openai_key)

    vectorStore = Chroma.from_documents(documents=documents, embedding=embedding)

    retrieved_docs = vectorStore.similarity_search_with_relevance_scores(query=q, k=1)

    most_relevant = retrieved_docs[0][0]
    most_relevant_score = float(retrieved_docs[0][1])

    if (most_relevant_score > 0.8):
        return most_relevant.page_content
    
    return ''
    
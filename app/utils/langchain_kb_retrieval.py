from app import db_cursor as cursor
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema.document import Document
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from app.config import Config

def kb_retrieve(q=''):
    # postgreSQL_select_Query = "select module_id, name from core_site_settings where module_id='chatplus'"
    # cursor.execute(postgreSQL_select_Query)
    # records = cursor.fetchall()
    kb = """
    phpFox is an open-source self-hosted social networking software that provides individuals and organizations with the tools to create an online social environment. The software provides an option to build up a social network similar to Facebook on a user’s own hosting and domain.
    phpFox comes with phpFox Store where third-party developers can submit and sell add-on apps, themes/templates and language packs.

    phpFox’s source code for the web is released by the company under an open-source license, which allowed a large community of developers to use the code as a foundation for creating and bringing new features for their users including extensions and themes to enhance the software’s capabilities.
    """

    separators = ["\n\n", "\n"]

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 255,
        chunk_overlap  = 20,
        length_function = len,
        separators=separators,
        # is_separator_regex = False,
    )

    documents = text_splitter.split_documents(documents=[Document(page_content=kb)])
    
    embedding = OpenAIEmbeddings(openai_api_key=Config.OPENAI_KEY)

    vectorStore = Chroma.from_documents(documents=documents, embedding=embedding)

    retrieved_docs = vectorStore.similarity_search(query=q, k=1)

    most_relevant = retrieved_docs[0]

    return most_relevant.page_content
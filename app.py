from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_openai import ChatOpenAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os
# things imported in notebook are all here
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

app = Flask(__name__) # flask intialization

# Loading the LLM
load_dotenv()

PINECONE_API_KEY=os.environ.get('PINECONE_API_KEY')
OPENAI_API_KEY=os.environ.get('OPENAI_API_KEY')

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# Loading embeddings and index
embeddings = download_hugging_face_embeddings()

index_name = "medical-chatbot" 
# Embed each chunk and upsert the embeddings into your Pinecone index.
docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)


# loading from Prompt

retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k":3})

memory = ConversationBufferMemory(return_messages=True)
chatModel = ChatOpenAI(model="gpt-4o")
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

question_answer_chain = create_stuff_documents_chain(chatModel, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)
conversation_chain = ConversationChain(llm=chatModel, memory=memory, verbose=True)



@app.route("/")
def index():
    return render_template('chat.html')


# when we click on send button, this following route is executed
@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg 
    print(input) # user message received here
    response = conversation_chain.run(input=msg)
    print("Response : ", response)
    return str(response)


# default route
if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True)

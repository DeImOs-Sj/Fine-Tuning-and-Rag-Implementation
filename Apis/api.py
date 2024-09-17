from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
# from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama

app = FastAPI(
    title="Olama Chatbot",
    version="0.1",
    description="This is a simple API that uses the Olama Chatbot",
) 

llm=Ollama(model="llama2")

prompt1=ChatPromptTemplate.from_template("You are helpful assistant.Please response to use queries\nQuestion:{question}")

add_routes(
    app,
    llm|prompt1,
    path="/ollama",
    )



if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)

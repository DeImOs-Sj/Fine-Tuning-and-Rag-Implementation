from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os 
from dotenv import load_dotenv


load_dotenv()


os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")    
os.environ["LANGCHAIN_TRACING_V2"]="true"

prompt=ChatPromptTemplate.from_messages(
    [("system","You are helpful assistant.Please response to use queries"),
     ("user","Question:{question}")]


)

st.title('Olama Chatbot')
input_text = st.text_input('Enter your question here:')


llm=Ollama(model="llama2")
output_parser=StrOutputParser()
chat=prompt|llm|output_parser

if input_text:
    st.write(chat.invoke({"question":input_text}))
# pip install streamlit langchain langchain-openai beautifulsoup4

import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def get_response(user_input):
    return "I don't know"


def get_vectorizer_from_url(url):
   # To get the text of webpage in document form
   loader=WebBaseLoader(url)
   document=loader.load()

   #split the document into chunk
   text_splitter= RecursiveCharacterTextSplitter() #intialzing the text splitter
   document_chunks=text_splitter.split_documents(document)
   
   return document_chunks


#app configuration
st.set_page_config(page_title="WEB-Ai_CHAT",page_icon="@")
st.title("chat with websites")
if "chat_history" not in st.session_state:
    st.session_state.chat_history =[
        AIMessage(content="Hello, I am a bot,How may I help you"),
    ]

#sidebar
with st.sidebar:
    st.header("Settings")
    website_url=st.text_input("Website Url")

if website_url is None or website_url=="":
    st.info("Please enter a URL") 

else: 
  documents= get_vectorizer_from_url(website_url)
  with st.sidebar:
     st.write(documents)
        
#user input
  user_query= st.chat_input("Type your message here...")
  if user_query is not None and user_query !="":
    response= get_response(user_query)
    st.session_state.chat_history.append(HumanMessage(content=user_query))
    st.session_state.chat_history.append(AIMessage(content=response))

#conversastion
for message in st.session_state.chat_history:
    if isinstance(message,AIMessage):
       with st.chat_message("AI"):
         st.write(message.content)
    elif isinstance(message,HumanMessage):
       with st.chat_message("Human"):
         st.write(message.content)

        
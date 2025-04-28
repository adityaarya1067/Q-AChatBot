import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

import os
from dotenv import load_dotenv

load_dotenv()
LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
LANGCHAIN_PROJECT = "Q&A Chatbot"

# Define the prompt
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries."),
        ("user", "question:{question}")
    ]
)

def generate_response(question, llm, api_key, temperature, max_tokens):
    # Initialize the ChatGroq model with the correct API key
    llm = ChatGroq(model=llm)
    
    # Instantiate the output parser
    output_parser = StrOutputParser()

    # Chain the components together (make sure this chaining method is valid in LangChain)
    chain = prompt | llm | output_parser
    
    # Invoke the chain to get the answer
    answer = chain.invoke({'question': question})
    
    return answer

st.title("Q&A Chatbot with GroqAPI")

# Sidebar for settings
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your GroqAPI Key:", type="password")

# Dropdown to select various models
llm = st.sidebar.selectbox("Select a model", ["llama3-70b-8192", "llama3-8b-8192", "gemma2-9b-it", "deepseek-r1-distill-llama-70b"])

# Adjust response parameters
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=100, value=150)

# Main interface for user input
st.write("Ask any question of your choice")
user_input = st.text_input("You:")

if user_input:
    response = generate_response(user_input, llm, api_key, temperature, max_tokens)
    st.write(response)
else:
    st.write("Please provide a query.")

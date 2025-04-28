<!-- Badges: Status, Version, Python, License -->
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen?style=for-the-badge)](https://github.com/your-org/groq-chatbot/actions)  
[![Version](https://img.shields.io/badge/version-1.0.0-blue?style=for-the-badge)](https://github.com/your-org/groq-chatbot/releases)  
[![Python](https://img.shields.io/badge/python-3.8%2B-blue?style=for-the-badge)](https://www.python.org/)  
[![License: MIT](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)](LICENSE)  

# Q&A Chatbot with GroqAPI

A Streamlit-based Q&A chatbot that uses Groq’s LLM to answer user questions.

---

## Features

- **Interactive UI**: Built with Streamlit for easy deployment and use :contentReference[oaicite:0]{index=0}.  
- **Model Selection**: Choose from multiple Groq models (`llama3-70b-8192`, `llama3-8b-8192`, `gemma2-9b-it`, `deepseek-r1-distill-llama-70b`) :contentReference[oaicite:1]{index=1}.  
- **Configurable Parameters**: Adjust temperature and max-token settings in real time.  
- **Prompt Chaining**: Uses LangChain’s `ChatPromptTemplate` and `StrOutputParser` to structure messages and parse results :contentReference[oaicite:2]{index=2}.  
- **Environment Variables**: Securely load your `LANGCHAIN_API_KEY` via a `.env` file using `python-dotenv` :contentReference[oaicite:3]{index=3}.

---

## Prerequisites

- Python 3.8+  
- [Streamlit](https://streamlit.io/)  
- [LangChain](https://github.com/langchain-ai/langchain)  
- [groq-python](https://pypi.org/project/groq-python/)  
- [python-dotenv](https://pypi.org/project/python-dotenv/)  

---
![Alt text](https://github.com/user-attachments/assets/b6c5974b-3bd9-4ff1-8701-b756f1d1ee83)



## Installation!


1. **Clone the repo**  
   ```bash
   git clone https://github.com/your-org/groq-chatbot.git
   cd groq-chatbot

   

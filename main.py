import streamlit as st
from langchain_ollama import ChatOllama

st.title('🤖 Make Your own chatbot with Langchain and Llama and Ollama!!!')


with st.form("llm-form"):
    text = st.text_area("Enter your question or statement:")
    submit = st.form_submit_button("Submit")

def generate_output(question):
    model = ChatOllama(model = "llama3.2:1b",base_url = "http://127.0.0.1:11434")
    response = model.invoke(question)
    return response.content

if "chat_history" not in st.session_state:
    st.session_state['chat_history'] = []


if submit and text:
    with st.spinner("Generating response..."):
        response = generate_output(text)
        st.session_state['chat_history'].append({"user": text, "ollama": response})
        st.write(response)

st.write("## Chat History")
for chat in reversed(st.session_state['chat_history']):
    st.write(f"**🧑 User**: {chat['user']}")
    st.write(f"**🧠 Assistant**: {chat['ollama']}")
    st.write("---")
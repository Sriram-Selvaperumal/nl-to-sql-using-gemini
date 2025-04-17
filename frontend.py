import streamlit as st
import random
import time
import backend

def response_generator(prompt):
    response = backend.GenerateResponse(prompt)
    for word in response.split():
        yield word + " "
        time.sleep(0.05)


st.title("Universal Human Langauage to SQL Query Converter ")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
   
    st.session_state.messages.append({"role": "user", "content": prompt})
   
    with st.chat_message("user"):
        st.markdown(prompt)

  
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator(prompt))
  
    st.session_state.messages.append({"role": "assistant", "content": response})

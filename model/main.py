import streamlit as strm
from chatBot import chatBot

CHATBOT = chatBot().generateChain()

strm.title("Travel chatbot")
prompt = strm.text_input("Pick a location")
if prompt:
    resp = CHATBOT.run(location = prompt)
    strm.write(resp)



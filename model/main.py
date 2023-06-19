import streamlit as strm
from chatBot import chatBot

CHATBOTCHAIN = chatBot().generateChains()

strm.title("Travel chatbot")
prompt = strm.text_input("Pick a location")
if prompt:
    for chain in CHATBOTCHAIN:
        c, title = chain
        strm.write(title)
        strm.write(c.run(location = prompt))



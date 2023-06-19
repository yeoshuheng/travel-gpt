import streamlit as strm
from chatBot import chatBot

CHATBOT = chatBot()

strm.title("Travel chatbot")
prompt = strm.text_input("Pick a location")

if prompt:
    resp = CHATBOT.checkInputs(prompt)
    if resp == "1":
        for chain in CHATBOT.generateChains():
            c, title = chain
            strm.write(title)
            strm.write(c.run(location = prompt))
    else:
        strm.write("The location added is not a valid location, please check your input again.")



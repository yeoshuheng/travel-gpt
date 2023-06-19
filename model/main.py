import streamlit as strm
from chatBot import chatBot

CHATBOT = chatBot()

strm.title("TravelGPT, your one-stop travel bot")
prompt = strm.text_input("Pick a location")

if prompt:
    resp = CHATBOT.checkInputs(prompt)
    if str(resp.strip()) == "1":
        for chain in CHATBOT.generateChains():
            c, title = chain
            strm.write(title)
            strm.write(c.run(location = prompt))
    else:
        strm.write("We cannot find the location you specified, please check your input.")


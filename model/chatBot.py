import os
from apikey import apikey
from langchain.llms import openai
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain
from userInput import userInput

os.environ["OPENAI_API_KEY"] = apikey

DEFAULT = {
    "temperature" : 0.9
}

class chatBot:
    def __init__(self, template : PromptTemplate = userInput().getTemplate(), params : dict = DEFAULT):
        self.llm = openai.OpenAI(temperature = params["temperature"])
        self.templates = []
        for t in template:
            self.templates.append(t)

    def generateChain(self):
        if len(self.templates) == 1:
            return LLMChain(llm = self.llm, prompt = self.templates[0], verbose = True)
        chainNeeded = []
        for i in self.templates:
            chainNeeded.append(LLMChain(llm = self.llm, prompt = i, verbose = True))
        return SimpleSequentialChain(chains = i)
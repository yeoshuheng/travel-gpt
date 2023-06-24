import os
from chat.apikey import apikey
from langchain.llms import openai
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain
from chat.templategen import TemplateGenerator

os.environ["OPENAI_API_KEY"] = apikey

DEFAULT = {
    "temperature" : 0.9
}

class chatBot:
    def __init__(self, template : list = TemplateGenerator().getTemplates(), params : dict = DEFAULT):
        self.llm = openai.OpenAI(temperature = params["temperature"])
        self.templateGen = TemplateGenerator()
        self.templates = []
        for t in template:
            self.templates.append(t)

    def generateChains(self) -> list:
        chains = []
        for i in self.templates:
            chains.append((LLMChain(llm = self.llm, prompt = i[0], verbose = True), i[1]))
        return chains
    
    def checkInputs(self, input) -> str:
        return LLMChain(llm = self.llm, 
            prompt = self.templateGen.getCheckTemplates()).run(location = input)
    
    def generateIternary(self, loc, day, month) -> str:
        return LLMChain(llm = self.llm, 
                        prompt = self.templateGen.iternaryGen(), 
                        verbose = True).run(location = loc, days = day, month = month)
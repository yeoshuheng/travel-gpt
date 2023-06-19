from langchain.prompts import PromptTemplate

class userInput:
    def __init__(self):
       pass
    
    def getTemplate(self) -> list:
        locprompt =  PromptTemplate(
            input_variables = ['location'],
            template = 'Give me a description of {location}'
        )

        return [locprompt]


    
from langchain.prompts import PromptTemplate

class TemplateGenerator:
    def __init__(self):
       pass
    
    def getTemplates(self) -> list:
       
        locprompt =  (PromptTemplate(
            input_variables = ['location'],
            template = 'Give me a description of {location}'
        ), "A BRIEF DESCRIPTION")

        hiddengems = (PromptTemplate(
            input_variables = ["location"],
            template = "Give me a list of hidden gems in {location} formatted nicely"
        ), "HIDDEN GEMS")

        cuisineinfo = (PromptTemplate(
            input_variables = ["location"],
            template = "I am tourist, give me 5 food recomendations that I must try when visiting {location}"
        ), "CUISINE")

        accomsinfo = (PromptTemplate(
            input_variables = ["location"],
            template = "I am tourist, give me 3 good accomodations at {location}"
        ), "ACCOMODATIONS")

        transportinfo = (PromptTemplate(
            input_variables = ["location"],
            template = "I am tourist, give me transport options when I am travelling at {location}"
        ), "GETTING AROUND")


        weatherinfo = (PromptTemplate(
            input_variables = ["location"],
            template = "What is the weather like at {location}"
        ), "WEATHER")

        return [locprompt, hiddengems, cuisineinfo, accomsinfo, transportinfo, weatherinfo]
    
    def getCheckTemplates(self) -> PromptTemplate:
        validLoc = PromptTemplate(
            input_variables = ["location"],
            template = "place = {location}, If place is fictional or does not exist, return 0. If place is real, return 1."
        )
        return validLoc


    
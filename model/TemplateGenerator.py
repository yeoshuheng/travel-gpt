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
            template = "Give me a list of the 5 best tourist attractions in {location} formatted nicely"
        ), "PLACES TO VISIT")

        cuisineinfo = (PromptTemplate(
            input_variables = ["location"],
            template = "I am tourist, give me 3 food recomendations that I must try when visiting {location}"
        ), "CUISINE")

        accomsinfo = (PromptTemplate(
            input_variables = ["location"],
            template = "I am tourist, give me 3 good accomodations at {location} along with their price per night"
        ), "ACCOMODATIONS")

        transportinfo = (PromptTemplate(
            input_variables = ["location"],
            template = "I am tourist, give me 3 best transport options when I am travelling at {location}"
        ), "GETTING AROUND")

        weatherinfo = (PromptTemplate(
            input_variables = ["location"],
            template = "What is the weather like at {location}"
        ), "WEATHER")

        ecotourism = (PromptTemplate(
            input_variables = ["location"],
            template = "I am a tourist, provide 2 ways on how to travel sustainably and reduce my carbon footprint during a trip to {location}."
        ), "TRAVEL SUSTAINABLY")

        return [locprompt, hiddengems, cuisineinfo, accomsinfo, transportinfo, weatherinfo, ecotourism]
    
    def getCheckTemplates(self) -> PromptTemplate:
        validLoc = PromptTemplate(
            input_variables = ["location"],
            template = "place = {location}, If place is fictional or cannot be found, return 0. If the place is not fictional and exists, return 1."
        )
        return validLoc


    
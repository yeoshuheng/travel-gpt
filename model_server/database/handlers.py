from chat.chatbot import chatBot

def handleDetails(inpt : str, bot : chatBot) -> dict:
    resp = {}
    for chain in bot.generateChains():
            c, title = chain
            c = c.run(location = inpt)
            resp[title] = c
    return resp

def handleIternary(inpt : tuple, bot : chatBot) -> dict:
      loc, day, month = inpt
      return {"iternary" : bot.generateIternary(loc, day, month)}

def mergeResponse(iter_resp : dict, det_resp : dict) -> dict:
      return iter_resp | det_resp

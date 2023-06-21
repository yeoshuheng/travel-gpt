from database.db import DB

def checkCache(k : str, db : DB) -> tuple:
    resp = db.read(k)
    if resp == None:
        return (False, {})
    return (True, resp)
import redis
import pickle

class DB:
    def __init__(self):
        pool = redis.ConnectionPool(host = 'redis', port = 6379)
        self.db = redis.Redis(connection_pool = pool)
    
    def write(self, k : str, v : dict) -> None:
        v = pickle.dumps(v)
        self.db.set(k, v)

    def read(self, k : str):
        resp = self.db.get(k)
        if resp == None:
            return resp
        resp = pickle.loads(resp)
        return resp

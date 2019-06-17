import re
import redis
from random import choice
from setting import REDIS_HOST,REDIS_PORT,REDIS_PASSWORD,REDIS_KEY,MAX_SCORE,MIN_SCORE,INITIAL_SCORE



class RedisClient(object):
    def __init__(self,host=REDIS_HOST,port=REDIS_PORT,password=REDIS_PASSWORD):
        self.db = redis.StrictRedis(host=host,port=port,password=password,decode_responses=True)

    def add(self,proxy,score=INITIAL_SCORE):
        if not re.match('\d+\.\d+\.\d+\.\d+\:\d+',proxy):
            return
        if not self.db.zscore(REDIS_KEY,proxy):
            return self.db.zadd(REDIS_KEY,score,proxy)

    def random_proxy(self):
        result = self.db.zrangebyscore(REDIS_KEY,MAX_SCORE,MAX_SCORE)
        if len(result):
            return choice(result)
        else:
            result = self.db.zrevrange(REDIS_KEY,0,100)
            if len(result):
                return choice(result)
            else:
                raise PoolEmptyError

    def decrease(self,proxy):
        return self.db.zrem(REDIS_KEY,proxy)

    def exists(self,proxy):
        return not self.db.zscore(REDIS_KEY,proxy) == None

    def max(self,proxy):
        return self.db.zadd(REDIS_KEY,MAX_SCORE,proxy)

    def count(self):
        return self.db.zcard(REDIS_KEY)

    def all(self):
        return self.db.zrangebyscore(REDIS_KEY,INITIAL_SCORE,MAX_SCORE)
    
        
        
            

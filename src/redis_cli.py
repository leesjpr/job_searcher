import redis

REDIS_SERVER = '192.168.57.110'
REDIS_PORT = 6379
REDIS_AUTH = 'job_searcher'
REDIS_DB = 0

class RedisCli():
    def __init__(self, addr, port, passwd, db):
        self.addr = addr
        self.port = port
        self.passwd = passwd
        self.db = db


    def connection(self):
        redis_cli = redis.Redis(host=self.addr, port=self.port, password=self.passwd)
        return redis_cli


if __name__ == '__main__':
    redis_cli = Redis_cli(REDIS_SERVER, REDIS_PORT, REDIS_AUTH, REDIS_DB).connection()


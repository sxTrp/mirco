import json

from redis.sentinel import Sentinel

redis_cli_conf = {
    "host-port": "10.10.1.82-26379,10.10.1.81-26379,10.10.1.80-26379",
    "pw": "bycx321!",
    "db": "27",
    "expire_time": 43200
}


class RedisException(Exception):
    pass


class Cache(object):
    def __init__(self, conf):
        self.conf = conf
        sentinel = self.get_sentinel_connect()
        if sentinel:
            self.master = sentinel.master_for('mymaster', socket_timeout=5)
            self.slave = sentinel.slave_for('mymaster', socket_timeout=2)
        self.cache_key_prefix = '{pj_name}_'.format(pj_name='ts')
        self.expire_time = conf['expire_time']

    def get_sentinel_connect(self):
        sentinel_host_info = self.parse_redis_conf(self.conf['host-port'])
        try:
            connect = Sentinel(sentinel_host_info, socket_timeout=2, password=redis_cli_conf['pw'],
                               decode_responses=True, db=self.conf['db'])
        except RedisException:
            connect = None

        return connect

    @staticmethod
    def parse_redis_conf(host_str):
        """
        将redis地址拼接成数组
        :param host_str:
        :return:
        """
        result = []
        for item in host_str.split(','):
            tmp_lst = item.split('-')
            host = str(tmp_lst[0].strip())
            post = int(tmp_lst[1].strip())
            result.append((host, post))
        return result

    def rpush(self, v, key='dms'):
        new_key = self.cache_key_prefix + key
        self.master.rpush(new_key, json.dumps(v))

    def lpop(self, key='dms'):
        new_key = self.cache_key_prefix + key
        result = self.master.lpop(new_key)
        if result:
            result = json.loads(result)
        return result

    def blpop(self, key='dms'):
        new_key = self.cache_key_prefix + key
        result = self.master.blpop(new_key)
        return result

    def expire(self, key, seconds):
        """
        设置过期时间
        :param key:
        :param seconds:
        :return:
        """
        new_key = self.cache_key_prefix + key
        self.master.expire(new_key, seconds)

    def flush(self):
        keys_lst = self.slave.keys(self.cache_key_prefix + '*')
        for key in keys_lst:
            self.master.delete(key)


redis_cli = Cache(redis_cli_conf)

if __name__ == '__main__':
    # redis_cli.rpush('1111111')
    # redis_cli.rpush('222')
    # redis_cli.rpush('333')
    print(redis_cli.blpop())

import redis
redis = redis.Redis(host='localhost', port=6379)


def redis_data():
    return redis



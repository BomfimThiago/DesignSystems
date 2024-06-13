from celery_worker import celery_app, redis_url
import redis

@celery_app.task
def fill_bucket():
    redis_client = redis.Redis.from_url(redis_url)
   
    lua_script = """
      local tokens_to_add = 5
      redis.call('SET', KEYS[1], tokens_to_add)
      return tokens_to_add
    """

    bucket_key = "bucket_key"
    result = redis_client.eval(lua_script, 1, bucket_key)
    print(f"Filled the bucket with 5 tokens. New token count: {result}")

import aioredis
from fastapi import FastAPI, Request, HTTPException
from celery_worker import redis_url

app = FastAPI()

BUCKET_KEY = "bucket_key"
TOKENS_PER_MINUTE = 5

# LUA script to check and decrement the token count
lua_script = """
local tokens = tonumber(redis.call("GET", KEYS[1]) or 0)
if tokens <= 0 then
    return -1
else
    redis.call("DECRBY", KEYS[1], 1)
    return tokens - 1
end
"""

# Redis client
redis_client = None

@app.on_event("startup")
async def startup_event():
    global redis_client
    redis_client = await aioredis.from_url(redis_url)

@app.on_event("shutdown")
async def shutdown_event():
    await redis_client.close()

@app.middleware("http")
async def verify_token_is_available_in_the_bucket(request: Request, call_next):
    global redis_client
    result = await redis_client.eval(lua_script, 1, BUCKET_KEY)

    if result == -1:
        raise HTTPException(status_code=429, detail="Too Many Requests")

    response = await call_next(request)
    return response

@app.get("/")
async def get_resource():
    return {"message": "Congrats, your request was succesfull!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

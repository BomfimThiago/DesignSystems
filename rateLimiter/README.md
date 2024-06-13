# Rate Limiter API Study

This project is a study of rate limiter APIs, specifically implementing a rate limiter using the token bucket technique with FastAPI. If you're interested in learning more about rate limiter concepts, you can refer to the [RateLimiter.md](./RateLimiter.md) file. I am currently exploring FastAPI, and I'm open to feedback or suggestions. Please reach out if you see any issues or have ideas for improvement.

## How This Project Works

Let's say that my system makes requests to an external API (an integration library), and each request to this external API costs money. I want to ensure that I do not spend too much money in a month. This type of rate limiter can prevent my API from receiving more requests than I am willing to pay for. For this, I am using the token bucket technique.

A task managed by Celery beat runs every minute, refilling the Redis bucket with 5 tokens. Each request (from any user) consumes one token from the bucket. If there are no tokens left, a 429 Too Many Requests response is returned. In this example, my API accepts only 5 requests per minute (in a real-world scenario, this could be 100, 1000, or any value that suits the business).

A middleware checks token availability before processing any request. The project uses LUA scripts for token management in Redis to prevent race conditions, ensuring requests are handled sequentially.

## Discussions

Here are some thoughts and questions that arose during the development of this project:

1. **User-Specific Rate Limiting:** If we want to limit the API by users (e.g., tracking by IP address), can we still use the token bucket technique, or would a time window technique be better? How can we restrict user requests without tracking request times, which might necessitate using the time window technique?

2. **Failure Scenarios:** What happens if the Celery beat worker goes down and the bucket is not refilled? In this project, the application will simply reject requests when tokens are depleted. Proper failure handling should be implemented.

3. **Failure Handling:** What is the best way to handle failures? Should we scale Redis and Celery horizontally to ensure availability, or use a fail-open approach where, if the rate limiter is down, all requests are allowed? The latter could defeat the purpose of rate limiting, especially if it's to control costs of external API usage.

## How to Run the Project

1. **Clone the Project:**
   ```bash
   git clone <repository-url>
   cd <project-directory>/rateLimiter```
2. **Build Docker Image**
   ```bash
    docker compose build

3. **Start the Containers**
   ```bash
    docker compose up
4. Access localhost:8000 if there is a token available you should see `{"message":"Congrats, your request was succesfull!"}`
if you make more then 5 requets(5 refreshes in the browser will do the trick) per minute you will see a server error message `Internal Server Error`

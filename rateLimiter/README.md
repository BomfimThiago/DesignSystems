# Rate Limiter

A rate limiter controls the number of retries, such as when attempting to unlock a phone by entering a password. Its primary purpose is to enhance security.

For example, YouTube enforces a limit of 20 video uploads per day. After reaching this limit, users must wait 24 hours before uploading more. This helps save storage and prevents any single user from consuming all available storage. Additionally, it allows for better prediction of storage needs and costs based on user activity.

## Designing a Rate Limiter

When designing a rate limiter, it's important to understand the business context and the specific requirements of the application. Key considerations include:

- **Define Functional Requirements:** Focus on the most critical aspects of the application.
- **Application Type:** Are you designing the rate limiter for a backend API, a single API, or a microservice?

For instance, an upload API or a comments API might use a rate limiter as middleware. If a user reaches the rate limit, the rate limiter will intercept requests and return a failure response, thereby throttling the user.

### Rate Limiter as a Microservice

Imagine the rate limiter as a microservice that intercepts requests before they reach the main application. It must manage latency, throughput, availability, and storage. The rules for the rate limiter service should be stored efficiently. For a per-user API rate limiter, you need to store all requests to count the number of requests made by each user within a given period.

### Failure Scenarios

- **Fail-open:** If the rate limiter goes down, everything continues as if the rate limiter didn't exist.
- **Fail-closed:** If the rate limiter goes down, all requests are stopped.

For more details on designing a rate limiter API, refer to this [link](https://medium.com/geekculture/system-design-design-a-rate-limiter-81d200c9d392).

## Advantages of a Rate Limiter

- Prevents DoS attacks by blocking excess calls.
- Reduces costs when using third-party API services charged per call.
- Reduces server load by filtering out excess requests caused by bots or user misbehavior.

## Rate Limiting Algorithms

### Token Bucket

According to the Stripe tech blog, the token bucket algorithm is used for rate limiting. This algorithm uses a centralized bucket host where tokens are taken on each request, and tokens are added back into the bucket at a controlled rate. If the bucket is empty, the request is rejected. Each Stripe user has a bucket, and tokens are removed from the bucket with every request. Rate limiters are implemented using Redis.

#### Example Use-Case

- Rate-limiting rules: 3 requests per user per minute.
- Requests within the limit are processed; excess requests return a 429 status code (Too Many Requests).

### Leaky Bucket Algorithm

The leaky bucket algorithm uses a first-in, first-out (FIFO) queue. Incoming requests are appended to the queue, and if there is no room, they are discarded. Requests are processed at regular intervals.

#### Parameters

- **Bucket size:** Queue size.
- **Outflow rate:** Number of requests processed at a fixed rate.

### Sliding Window Rate Limiter

This algorithm tracks request timestamps, typically using cache (e.g., Redis sorted sets). When a new request arrives, outdated timestamps are removed. If the log size is within the allowed count, the request is accepted; otherwise, it is rejected.

### Fixed Time Window

In a fixed window counter, fixed-size time frames are created, each with a counter responsible for counting hits within that period. If the number of hits exceeds the threshold, all requests in that window are discarded.

## Real-World Examples

### GitHub

GitHub uses a rate-limiting strategy to manage the API usage of its users. For unauthenticated requests, the rate limit is 60 requests per hour. For authenticated requests, the limit increases to 5,000 requests per hour. This prevents abuse of their API and ensures fair usage among users.

- **More info:** [GitHub Rate Limiting](https://docs.github.com/en/rest/overview/resources-in-the-rest-api#rate-limiting)

### Twitter

Twitter’s API imposes rate limits on all API endpoints to ensure that their service remains available to all users. Different types of requests have different rate limits, such as 300 requests per 15 minutes for user timelines.

- **More info:** [Twitter Rate Limiting](https://developer.twitter.com/en/docs/basics/rate-limits)

### Google Maps

Google Maps API enforces a rate limit to control the number of requests a user can make within a certain time frame. This helps to protect their infrastructure from overload and ensures consistent performance for all users.

- **More info:** [Google Maps API Rate Limits](https://developers.google.com/maps/documentation/geocoding/usage-and-billing)

## Conclusion

Rate limiting is essential for maintaining the performance and security of applications. Understanding the business context and carefully designing the rate limiter can ensure efficient and reliable operation.

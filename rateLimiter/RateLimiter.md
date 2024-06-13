# Considerations
This is a study about rate limiter, it's not a truth fontain. So if you see something wrong please
reach out to me, I would be gladly to address that.

This is an amazing link about rate limiter api:
[link](https://medium.com/geekculture/system-design-design-a-rate-limiter-81d200c9d392).


# Rate Limiting: Ensuring Fair and Secure API Usage

Rate limiting is a crucial strategy for managing the usage of APIs, database queries, and network data transmission. By restricting the number of requests within a specified time frame, rate limiting helps maintain security, conserve resources, and ensure fair access for all users.

## Understanding Rate Limiting

- **Definition:** Rate limiting restricts the number of requests per user within a defined period.
- **Example:** YouTube limits users to 20 video uploads per day, after which they must wait 24 hours to upload more videos.

## Design Considerations

- **Functional Requirements:** Focus on critical aspects of the application.
- **Application Type:** Consider the specific needs of the application, such as API endpoints, database queries, or network transmission limits.

## Implementing Rate Limiting

### Token Bucket Algorithm

- **Description:** Tokens are used to control the rate of requests. Each request consumes a token, and tokens are replenished at a controlled rate.
- **Example Use-Case:** Limiting users to 3 requests per minute.

### Leaky Bucket Algorithm

- **Description:** Requests are added to a queue and processed at a fixed rate. Excess requests are discarded.
- **Parameters:** Bucket size (queue size) and outflow rate (rate of request processing).

### Sliding Window Rate Limiter

- **Description:** Tracks request timestamps to ensure requests are within the allowed count for a specific time frame.

### Fixed Time Window

- **Description:** Divides time into fixed-size windows, with each window having a counter for counting hits. Requests exceeding the threshold are discarded.

## Real-World Examples

- **GitHub:** Limits unauthenticated requests to 60 per hour and authenticated requests to 5,000 per hour.
- **Twitter:** Imposes rate limits on user timelines to ensure fair API usage.
- **Google Maps:** Enforces rate limits to protect its infrastructure and maintain consistent performance.

## Conclusion

Rate limiting is essential for maintaining the performance and security of applications. By carefully designing rate limiters and understanding the business context, developers can ensure efficient and reliable operation of their applications.

# HTTP Response Status Codes

This document provides a comprehensive list of HTTP response status codes with their standard reason phrases, as defined by the Internet Assigned Numbers Authority (IANA) and RFC 9110. HTTP status codes are three-digit numbers issued by a server in response to a client’s request, indicating the outcome of the request. They are grouped into five classes based on the first digit. This list is organized by class for clarity and is intended for inclusion in the HTTP Overview folder of the MCP section.

---

## 1xx: Informational
These codes indicate a provisional response, communicating request progress. No message body is included.

- **100 Continue**: The server has received the request headers, and the client should proceed to send the request body.  
- **101 Switching Protocols**: The server is switching protocols as requested by the client (e.g., to WebSockets).  
- **102 Processing**: The server has received the request and is processing it, but no response is available yet (used in WebDAV).  
- **103 Early Hints**: Preliminary headers are sent to allow the client to preload resources before the final response.  

---

## 2xx: Success
These codes indicate that the client’s request was successfully received, understood, and accepted.

- **200 OK**: The request was successful, and the response contains the requested resource.  
- **201 Created**: The request was fulfilled, resulting in a new resource being created.  
- **202 Accepted**: The request has been accepted for processing, but processing is not complete.  
- **203 Non-Authoritative Information**: The response contains metadata from a third-party source, not the origin server.  
- **204 No Content**: The request was successful, but there is no content to return (e.g., for a DELETE request).  
- **205 Reset Content**: The server instructs the client to reset the document view (e.g., clear a form).  
- **206 Partial Content**: The server is delivering only part of the resource due to a range request.  
- **207 Multi-Status**: Provides status for multiple independent operations (used in WebDAV).  
- **208 Already Reported**: Used in WebDAV to avoid enumerating the same collection bindings repeatedly.  
- **226 IM Used**: The server has fulfilled a GET request with instance manipulations applied (e.g., delta encoding).  

---

## 3xx: Redirection
These codes indicate that further action is needed to complete the request, often involving a redirect to another URI.

- **300 Multiple Choices**: The request has multiple possible responses; the client should choose one.  
- **301 Moved Permanently**: The resource has been permanently moved to a new URI, specified in the Location header.  
- **302 Found**: The resource is temporarily located at another URI; the client should use the original method.  
- **303 See Other**: The response is at another URI, and the client should use a GET request to access it.  
- **304 Not Modified**: The resource has not been modified since the client’s last request (used for caching).  
- **305 Use Proxy**: The resource must be accessed through a proxy specified in the Location header (deprecated).  
- **307 Temporary Redirect**: Similar to 302, but the client must not change the HTTP method.  
- **308 Permanent Redirect**: Similar to 301, but the client must not change the HTTP method.  

---

## 4xx: Client Error
These codes indicate an error due to a problem with the client’s request, such as bad syntax or lack of authorization.

- **400 Bad Request**: The server cannot process the request due to invalid syntax or malformed data.  
- **401 Unauthorized**: The client must authenticate itself to access the resource (implies “unauthenticated”).  
- **402 Payment Required**: Reserved for future use (e.g., digital payment systems; rarely used).  
- **403 Forbidden**: The client is authenticated but lacks permission to access the resource.  
- **404 Not Found**: The server cannot find the requested resource.  
- **405 Method Not Allowed**: The request method is not supported for the resource (e.g., GET on a POST-only endpoint).  
- **406 Not Acceptable**: The server cannot provide a response matching the client’s Accept headers.  
- **407 Proxy Authentication Required**: The client must authenticate with a proxy to proceed.  
- **408 Request Timeout**: The server timed out waiting for the client’s request.  
- **409 Conflict**: The request conflicts with the current state of the resource (e.g., version conflict in PUT).  
- **410 Gone**: The resource is permanently unavailable with no forwarding address.  
- **411 Length Required**: The request lacks a valid Content-Length header.  
- **412 Precondition Failed**: The server does not meet preconditions specified in the request headers.  
- **413 Payload Too Large**: The request body is larger than the server can process.  
- **414 URI Too Long**: The requested URI exceeds the server’s length limit.  
- **415 Unsupported Media Type**: The request’s media format is not supported by the server.  
- **416 Range Not Satisfiable**: The requested range cannot be fulfilled by the server.  
- **417 Expectation Failed**: The server cannot meet the requirements of the Expect header.  
- **418 I’m a teapot**: A humorous code indicating the server refuses to brew coffee (from an April Fool’s RFC).  
- **421 Misdirected Request**: The request was sent to a server unable to produce a response.  
- **422 Unprocessable Entity**: The request is well-formed but cannot be processed due to semantic errors (WebDAV).  
- **423 Locked**: The resource is locked and cannot be accessed (WebDAV).  
- **424 Failed Dependency**: The request failed due to the failure of a related request (WebDAV).  
- **426 Upgrade Required**: The client must use a different protocol (e.g., TLS/1.0).  
- **428 Precondition Required**: The server requires conditional headers (e.g., If-Match) to process the request.  
- **429 Too Many Requests**: The client has sent too many requests in a given time (rate limiting).  
- **431 Request Header Fields Too Large**: The request headers exceed the server’s size limit.  
- **451 Unavailable For Legal Reasons**: The resource is blocked due to legal restrictions.  

---

## 5xx: Server Error
These codes indicate that the server failed to fulfill a valid request due to an internal error.

- **500 Internal Server Error**: A generic error indicating the server encountered an unexpected condition.  
- **501 Not Implemented**: The server does not support the functionality required for the request.  
- **502 Bad Gateway**: The server, acting as a gateway, received an invalid response from an upstream server.  
- **503 Service Unavailable**: The server is temporarily unavailable, often due to maintenance or overloading.  
- **504 Gateway Timeout**: The server, acting as a gateway, did not receive a timely response from an upstream server.  
- **505 HTTP Version Not Supported**: The HTTP version in the request is not supported by the server.  
- **506 Variant Also Negotiates**: The server’s chosen resource is configured to negotiate, causing a conflict.  
- **507 Insufficient Storage**: The server cannot store the data needed to complete the request (WebDAV).  
- **508 Loop Detected**: The server detected an infinite loop while processing the request (WebDAV).  
- **510 Not Extended**: Further extensions to the request are required for the server to fulfill it.  
- **511 Network Authentication Required**: The client must authenticate to access the network.  

---

## Notes

- This list includes all standard HTTP status codes as of RFC 9110 and IANA’s registry, ensuring completeness for academic use.  
- Non-standard codes (e.g., 420, 450) used by specific platforms like Twitter or Microsoft are excluded for brevity but can be added if required.  

For further details, refer to:  
- [IANA HTTP Status Code Registry](https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml)  
- [RFC 9110](https://datatracker.ietf.org/doc/html/rfc9110)  

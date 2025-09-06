# HTTP Response Status Codes (Table Format)

| Code | Reason Phrase                     | Description |
|------|-----------------------------------|-------------|
| **1xx – Informational** | | |
| 100  | Continue                          | Request headers received; client should send body. |
| 101  | Switching Protocols               | Server switching protocols (e.g., WebSockets). |
| 102  | Processing                        | Request being processed; no response yet (WebDAV). |
| 103  | Early Hints                       | Preliminary headers for preloading resources. |
| **2xx – Success** | | |
| 200  | OK                                | Request succeeded; resource included. |
| 201  | Created                           | Request created a new resource. |
| 202  | Accepted                          | Request accepted, processing pending. |
| 203  | Non-Authoritative Information     | Response metadata from third-party, not origin. |
| 204  | No Content                        | Success, no response body (e.g., DELETE). |
| 205  | Reset Content                     | Client should reset document view. |
| 206  | Partial Content                   | Partial response to a range request. |
| 207  | Multi-Status                      | Multiple status codes for independent operations (WebDAV). |
| 208  | Already Reported                  | Resource already reported in WebDAV. |
| 226  | IM Used                           | Resource delivered with delta encoding. |
| **3xx – Redirection** | | |
| 300  | Multiple Choices                  | Multiple response options available. |
| 301  | Moved Permanently                 | Resource moved permanently to a new URI. |
| 302  | Found                             | Resource temporarily located at different URI. |
| 303  | See Other                         | Resource available at another URI; use GET. |
| 304  | Not Modified                      | Resource not modified (caching). |
| 305  | Use Proxy                         | Access through proxy (deprecated). |
| 307  | Temporary Redirect                | Redirect; method must not change. |
| 308  | Permanent Redirect                | Permanent redirect; method must not change. |
| **4xx – Client Error** | | |
| 400  | Bad Request                       | Invalid syntax or malformed request. |
| 401  | Unauthorized                      | Authentication required. |
| 402  | Payment Required                  | Reserved for future use. |
| 403  | Forbidden                         | Client authenticated but not authorized. |
| 404  | Not Found                         | Resource not found. |
| 405  | Method Not Allowed                | Method not supported for resource. |
| 406  | Not Acceptable                    | No response matches client’s Accept headers. |
| 407  | Proxy Authentication Required     | Authentication required with proxy. |
| 408  | Request Timeout                   | Client request timed out. |
| 409  | Conflict                          | Request conflicts with resource state. |
| 410  | Gone                              | Resource permanently removed. |
| 411  | Length Required                   | Missing Content-Length header. |
| 412  | Precondition Failed               | Request conditions not met. |
| 413  | Payload Too Large                 | Request body too large. |
| 414  | URI Too Long                      | Request URI too long. |
| 415  | Unsupported Media Type            | Request media type not supported. |
| 416  | Range Not Satisfiable             | Invalid range request. |
| 417  | Expectation Failed                | Cannot meet `Expect` header requirements. |
| 418  | I’m a teapot                      | Joke status; server refuses to brew coffee. |
| 421  | Misdirected Request               | Request sent to wrong server. |
| 422  | Unprocessable Entity              | Well-formed but semantically invalid (WebDAV). |
| 423  | Locked                            | Resource locked (WebDAV). |
| 424  | Failed Dependency                 | Request failed due to related request (WebDAV). |
| 426  | Upgrade Required                  | Client must use a different protocol. |
| 428  | Precondition Required             | Requires conditional request headers. |
| 429  | Too Many Requests                 | Rate limiting applied. |
| 431  | Request Header Fields Too Large   | Request headers too large. |
| 451  | Unavailable For Legal Reasons     | Resource blocked by legal restriction. |
| **5xx – Server Error** | | |
| 500  | Internal Server Error             | Generic server error. |
| 501  | Not Implemented                   | Server does not support request functionality. |
| 502  | Bad Gateway                       | Invalid response from upstream server. |
| 503  | Service Unavailable               | Server temporarily overloaded/unavailable. |
| 504  | Gateway Timeout                   | Upstream server did not respond. |
| 505  | HTTP Version Not Supported        | Request HTTP version not supported. |
| 506  | Variant Also Negotiates           | Content negotiation conflict. |
| 507  | Insufficient Storage              | Server storage insufficient (WebDAV). |
| 508  | Loop Detected                     | Infinite loop detected (WebDAV). |
| 510  | Not Extended                      | Further extensions required. |
| 511  | Network Authentication Required   | Client must authenticate to access network. |

---
## Notes

- This list includes all standard HTTP status codes as of RFC 9110 and IANA’s registry, ensuring completeness for academic use.  
- Non-standard codes (e.g., 420, 450) used by specific platforms like Twitter or Microsoft are excluded for brevity but can be added if required.

---

## References
   For further details, refer to:  
- [IANA HTTP Status Code Registry](https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml)  
- [RFC 9110](https://datatracker.ietf.org/doc/html/rfc9110)




 

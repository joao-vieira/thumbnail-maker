### Thumbnail Maker

## Description
This API receives an image in Base64 format, and resizes it to 100x100px. Since image processing can take time, a long-running job architecture was implemented. For the purpose of this exercise, a simple implementation with the library flask_executor was implemented.

## How to Use
To start the server, run `docker-compose up`

## Requests
The server receives POST requests in the form of "/image" and resizes the image. Once the image is ready, it can be requested with a GET request at "/result"

Example image request:
`curl -X POST -d "image=iVBORw0KGgoAAAANSUhEUgAAABIAAAAPCAIAAABm5AhFAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAFiUAABYlAUlSJPAAAAA6SURBVDhPY/hPFhiS2hgYCIsAwcA6kkhADW1YfY8M4ArQteHSiSaFrggijRVAVYABdrMJAnpq%2B/8fAFBw9CiMWfoDAAAAAElFTkSuQmCC" "http://localhost:5000/image"`

Example result request:
`curl "http://localhost:5000/result"`
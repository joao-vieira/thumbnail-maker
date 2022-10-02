### Thumbnail Maker

## Description
This API receives an image in Base64 format, and resizes it to 100x100px. Since image processing can take time, a long-running job architecture was implemented. For the purpose of this exercise (and due to time constraints), a very simple implementation with the library flask_executor to allow one image to be processed at a time was implemented.

## How to Use
To start the server, run `docker-compose up`

## Requests
The server receives POST requests in the form of "/image" and resizes the image. Once the image is ready, it can be requested with a GET request at "/result"

Example image request:
`curl -X POST -d "image=iVBORw0KGgoAAAANSUhEUgAAABIAAAAPCAIAAABm5AhFAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAFiUAABYlAUlSJPAAAAA6SURBVDhPY/hPFhiS2hgYCIsAwcA6kkhADW1YfY8M4ArQteHSiSaFrggijRVAVYABdrMJAnpq%2B/8fAFBw9CiMWfoDAAAAAElFTkSuQmCC" "http://localhost:5000/image"`

Example result request:
`curl "http://localhost:5000/result"`

## Tests
In order to run tests, just type `pytest` while locally in the thumbnail-maker directory. Currently only one example image is tested, in a production environment we would test edge cases like a 1x1px image or very large images. 

## Dependencies and Libraries
I chose Flask for setting up the basic API structure. flask_executor was used for the long-running job architecture, since its futures library allows users to retrieve results only when they are ready. Pillow was the library chosen for image processing, since it contains a good resize function. Pytest was used for testing.

## Possible improvements
- When it comes to making a long-running job architecture, with more time I would have liked to incorporate the use of Redis and Celery, creating queue-based workers.
- A logging system would be essential to debugging the API in a production environment.
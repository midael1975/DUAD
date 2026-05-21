# Part 4: Technical Explanation 🧠

Create a README.md file (or text document) that includes:

1. Selected API
Art Institute of Chicago API (AIC API)
A public API that allows you to query information on thousands of artworks, artists, and collections in the museum. It does not require authentication and responds in JSON.

1. GET – List of Works
Method: GET

Endpoint:

Code: 200 Ok
`https://api.artic.edu/api/v1/artworks`
Description: Retrieves a paginated list of artworks.

Response (example):

json
{
"data": [

{
"id": 27992,
"title": "The Bedroom",

"artist_display": "Vincent van Gogh"

}
]
}

GET – Specific Artwork
Method: GET

Endpoint:

Code: 200 Ok
`https://api.artic.edu/api/v1/artworks/129884`
Description: Retrieves detailed information about an artwork.

Response:

json
{
"data": {
"id": 129884,

"title": "Water Lilies",

"artist_display": "Claude Monet"

}
}

   What I Learned

How to consume a real API from Postman.

How to interpret JSON responses.

How GET, POST, and PUT methods work (The post, put and delete are not allowed on this public APIs)

How to parse HTTP status codes.

How to work with collections and environments in Postman.

How to use a test service when the real API doesn't allow writing.

  Final Reflection 🧭

In 1 or 2 paragraphs, answer:
What did you learn about how APIs work?
APIs allow two software systems to work together for a purpose that is useful to us, since they allow us to access data and functionalities quickly and efficiently through applications that make our lives easier.

How did Postman help you understand communication between the client and the server?
It helped me see what the client requires, what the server displays, test with different results, and view and analyze status codes, headers, and JSON.

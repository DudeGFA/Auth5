# API Documentation

## Overview
This API allows users to retrieve data records from the Web5 blockchain by providing a set of data keys. The data keys are used to identify specific records associated with decentralized identifiers (DIDs).

**Base URL:** `https://auth5js.onrender.com`

## Endpoints

### POST `/`
#### Description
Retrieve data records from the Web5 blockchain based on provided DIDs and record IDs.

#### Request
- **Method:** `POST`
- **Content Type:** `application/json`
- **Body:**
  ```json
  {
    "key1": {
      "did": "web5-did-1",
      "recordId": "record-id-1"
    },
    "key2": {
      "did": "web5-did-2",
      "recordId": "record-id-2"
    },
    ...
  }
  ```

#### Response
- **Success Response:**
  - **Status Code:** `200 OK`
  - **Body:**
    ```json
    {
      "key1": "data-text-1",
      "key2": "data-text-2",
      ...
    }
    ```
- **Error Responses:**
  - **Status Code:** `400 Bad Request`
    - **Body:**
      ```json
      {
        "error": "Bad Request - Incomplete or Malformed Data"
      }
      ```
  - **Status Code:** `500 Internal Server Error`
    - **Body:**
      ```json
      {
        "error": "Internal Server Error"
      }
      ```

## Usage
To use this API, send a POST request to the `/` endpoint with a JSON object containing data keys, each specifying a DID and a record ID. The API will fetch the corresponding records from the Web5 blockchain and return a JSON object with the data associated with each key.

### Example

#### Request
```http
POST https://auth5js.onrender.com/
Content-Type: application/json

{
  "user1": {
    "did": "web5-did-123",
    "recordId": "record-id-123"
  },
  "user2": {
    "did": "web5-did-456",
    "recordId": "record-id-456"
  }
}
```

#### Response
```json
{
  "user1": "User 1 data",
  "user2": "User 2 data"
}
```

## Notes
- The API assumes that the provided DIDs and record IDs are valid and exist on the Web5 blockchain.
- The base URL for the API is `https://auth5js.onrender.com`.
- The API logs internal errors to the console and returns appropriate HTTP status codes in the response.

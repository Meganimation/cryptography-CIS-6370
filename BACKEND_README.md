# Backend API

A simple Flask backend that provides a `/hello` endpoint for managing greeting messages.

## Features

- **GET /hello**: Retrieve the current greeting message
- **POST /hello**: Update the greeting message
- **SQLite Database**: Stores greeting messages with timestamps
- **Health Check**: GET /health endpoint for monitoring

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the backend:
```bash
python backend.py
```

The server will start on `http://localhost:5000`

## API Endpoints

### GET /hello
Retrieves the current greeting message.

**Response:**
```json
{
  "greetingMsg": "hello world!"
}
```

### POST /hello
Updates the greeting message.

**Request Body:**
```json
{
  "greetingMsg": "Your new greeting message"
}
```

**Response:**
```json
{
  "message": "Greeting updated successfully",
  "greetingMsg": "Your new greeting message"
}
```

### GET /health
Health check endpoint.

**Response:**
```json
{
  "status": "healthy"
}
```

## Testing

Run the test script to verify the endpoints work correctly:

```bash
python test_backend.py
```

Make sure the backend is running before executing the tests.

## Database

The backend uses SQLite with a `greeting.db` file. The database automatically initializes with a default "hello world!" message if no greeting exists.

## Error Handling

- Returns 400 for invalid request data
- Returns 500 for server errors
- Validates that greetingMsg is a non-empty string

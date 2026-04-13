# Password Strength Checker API

A REST API built with FastAPI that checks the strength of a password.

## What it does
- Returns a strength score (weak / fair / strong)
- Tells you what is missing in your password
- Returns estimated crack time

## How to run locally

1. Install dependencies
pip install fastapi uvicorn

2. Run the server
fastapi run

3. Open in browser
http://127.0.0.1:8000/docs

## API Endpoints

POST /password_check
Send a password, get back strength analysis.

Request body:
{
  "password": "Hello@123"
}

Response:
{
  "score": 5,
  "strength": "strong",
  "missing": [],
  "crack_time": "Would take years"
}
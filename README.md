# Password Strength Checker API

A REST API built with FastAPI that checks the strength of a password.

## What it does
- Returns a strength score (weak / fair / strong)
- Tells you what is missing in your password
- Returns estimated crack time

## Live Demo
Base URL: https://password-strength-checker-80by.onrender.com
API Docs: https://password-strength-checker-80by.onrender.com/docs

## Tech Stack
- Python
- FastAPI
- Deployed on Render

## How to run locally

1. Clone the repository
```bash
git clone https://github.com/prerna12github/password-strength-checker.git
cd password-strength-checker
```

2. Install dependencies
```bash
pip install fastapi[standard]
```
3. Run the server
```bash
fastapi dev main.py
```

4. Open in browser
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

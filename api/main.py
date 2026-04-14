from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import re

app = FastAPI()

class Password(BaseModel):
    password: str

@app.get("/")
def read_root():
    return {"message": "Welcome Users"}

@app.post("/password_check")
async def pass_check(password: Password):
    score = 0
    missing = []
    pwd = password.password

    if not pwd:
        raise HTTPException(status_code=400, detail="Password cannot be empty")
    if pwd.strip() == "":
        raise HTTPException(status_code=400, detail="Password cannot contain only spaces")
    if " " in pwd:
        raise HTTPException(status_code=400, detail="Password cannot contain spaces")

    if len(pwd) >= 8:
        score += 1
    else:
        missing.append("Password must have atleast 8 characters")
    if len(pwd) >= 12:
        score += 1
    if re.search(r"[a-z]", pwd):
        score += 1
    else:
        missing.append("Password must have atleast 1 lowercase letter")
    if re.search(r"[A-Z]", pwd):
        score += 1
    else:
        missing.append("Password must have atleast 1 uppercase letter")
    if re.search(r"\d", pwd):
        score += 1
    else:
        missing.append("Password must have atleast 1 digit")
    if re.search(r"[@$!%*?&]", pwd):
        score += 1
    else:
        missing.append("Password must have atleast 1 special character")

    return {"score": score, "missing": missing}

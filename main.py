from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import re

class Password(BaseModel):
    password:str


app = FastAPI()

@app.get("/")
def read_root():
    return {"Welcome": "Users"}

@app.post("/password_check")
async def pass_check(password:Password):
    score=0
    missing=[]
    pwd=password.password
  
    if not pwd:
      raise HTTPException(status_code=400, detail="Password cannot be empty")

    if pwd.strip() == "":
      raise HTTPException(status_code=400, detail="Password cannot contain only spaces")

    if " " in pwd:
      raise HTTPException(status_code=400, detail="Password cannot contain spaces")
  
    if len(pwd)>=8:
        score+=1
    else:
        missing.append("Password must have atleast 8 characters")
    if len(pwd)>=12:
        score+=1
    if re.search(r"[a-z]",pwd):
        score+=1
    else:
        missing.append("Passward must have atleast 1 lowercase letter")  
    if re.search(r"[A-Z]",pwd):
        score+=1
    else:
        missing.append("Password must have atleast 1 uppercase letter")
    if re.search(r"\d",pwd):
        score+=1
    else:
        missing.append("Password must have atleast 1 digit")
    if re.search(r"[@$!%*?&]",pwd):
        score+=1
    else:
        missing.append("Password must have atleast 1 special character")     

    if score<=2:
        strength="weak" 
    elif score<=4:
        strength="fair"
    else:
        strength="strong"

    crack_times = {
        0: "Crackable instantly",
        1: "Crackable in seconds",
        2: "Crackable in minutes",
        3: "Crackable in a few hours",
        4: "Crackable in days",
        5: "Would take years",
        6: "Would take centuries",
    }

    return {
        "score": score,
        "strength": strength,
        "missing": missing,
        "crack_time": crack_times[score]
    }
                      
                 
                 
               



     

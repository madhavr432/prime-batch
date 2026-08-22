from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class NameRequest(BaseModel):
    name: str

@app.post("/greet")
def greet_user(request: NameRequest):
    return {"message": f"Hello, {request.name}!"}

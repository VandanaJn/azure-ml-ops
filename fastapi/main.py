from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
from transformers import pipeline

gp2_generator=pipeline("text-generation",model="gpt2")
class Body(BaseModel):
    text:str

app=FastAPI()
@app.get("/", response_class=FileResponse)
def root():
    return FileResponse("static/index.html")

@app.post("/generate")
def generate(body:Body):
    return JSONResponse(gp2_generator(body.text)[0])

#to run locally
#change directory to fastapi and run following
#uvicorn --host 0.0.0.0 main:app
#browse http://127.0.0.1 and enjoy generating text



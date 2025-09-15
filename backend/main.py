from fastapi import FastAPI

app = FastAPI()

@app.get("/healthy")
def check_env():
    return {"ok":True}
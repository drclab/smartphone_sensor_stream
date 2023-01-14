from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    return "Dulun Research & Consulting"
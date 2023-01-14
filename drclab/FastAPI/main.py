from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    return "Dulun Research & Consulting"

@app.get('/item/{id}')
def read_item(id: Int):
    return id
from fastapi import FastAPI

app = FastAPI()


@app.get("/") # DEFINES THE path
def root():
    return {"message": "Hello World"}
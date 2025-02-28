from fastapi import FastAPI
from app.agent import graph

app = FastAPI()


@app.get("/")
def read_root():
    return graph.invoke({"customer_name": "John Doe","my_var": "Hello"})

# To run - fastapi dev app/api.py



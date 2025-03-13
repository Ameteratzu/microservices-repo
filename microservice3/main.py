from fastapi import FastAPI

app = FastAPI()

@app.get("/orders")
def get_orders():
    return {"orders": ["Order1", "Order2", "Order3"]}
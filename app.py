from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
import os

load_dotenv()

from routes.fare import router as fare_router

app = FastAPI(
    title="Uber Clone API",
    description="A simple fare estimation API",
    version="1.0.0"
)

# Serve static files (HTML, CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Default route to return index.html
@app.get("/")
def root():
    return FileResponse("static/index.html")

# Register your API routes
app.include_router(fare_router)

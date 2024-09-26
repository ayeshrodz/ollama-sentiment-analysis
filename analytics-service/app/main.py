from fastapi import FastAPI
from .routers import analyze

# Initialize the FastAPI app
app = FastAPI()

# Include routers
app.include_router(analyze.router)

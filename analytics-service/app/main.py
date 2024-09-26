from fastapi import FastAPI
from .routers import analyze
import logging

# Initialize the logger
logger = logging.getLogger(__name__)

# Initialize the FastAPI app
app = FastAPI()

# Log that the application has started
logger.info("Starting FastAPI application...")

# Include routers
app.include_router(analyze.router)

@app.on_event("startup")
async def startup_event():
    logger.info("Application startup complete.")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Application shutdown complete.")

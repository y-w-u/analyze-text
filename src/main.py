import logging

from fastapi import FastAPI
from src.routers import text_analysis

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

app.include_router(text_analysis.router, prefix="/analyze-text")

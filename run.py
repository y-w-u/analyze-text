from src.main import app
from src.config import config
import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host=config.APP_HOST, port=config.APP_PORT)

import uvicorn
from fastapi import FastAPI
from app.api import api_router
from app.db import database

app = FastAPI(
    docs_url="/api/docs",
)

app.include_router(api_router, prefix="/api")


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

if __name__ == "__main__":
  uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")

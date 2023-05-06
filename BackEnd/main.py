from fastapi import FastAPI, Depends
from .database import get_db
from .Routers import login
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

HWBackend = FastAPI()

@HWBackend.get("/")
def hello():
    print("done")
    return {"done":"done"}

HWBackend.include_router(login.router)
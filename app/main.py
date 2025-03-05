from fastapi import FastAPI
from . import models
from .database import engine
from .routers import users, tasks, auth
from . config import settings
    
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(tasks.router)
app.include_router(auth.router)




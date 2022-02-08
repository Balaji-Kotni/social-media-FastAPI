from fastapi import FastAPI
from .routers import users, posts, auth, votes
from . import models
from .database import engine
# for defalting the hasing algorthem


models.Base.metadata.create_all(bind=engine)


app = FastAPI()


app.include_router(auth.router)
app.include_router(posts.router)
app.include_router(users.router)
app.include_router(votes.router)


@app.get('/')
def home():
    return "Welcome to my API"
# create user

from fastapi import FastAPI
from router import router # import the APIRouter instance

app = FastAPI() # create FASTAPI application instance

app.include_router(router=router) # Mount the router to include / users endpoint

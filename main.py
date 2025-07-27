from fastapi import FastAPI
from routes.Users import router as user_router
from routes.Tasks import router as task_router

app = FastAPI()
app.include_router(user_router)
app.include_router(task_router)

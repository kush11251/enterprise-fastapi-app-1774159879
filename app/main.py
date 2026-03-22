from fastapi import FastAPI
from app.controllers import user_controller

app = FastAPI(title="Enterprise Blueprint")

app.include_router(user_controller.router, prefix="/users", tags=["users"])

@app.get("/status")
def status():
    '''Health check endpoint'''
    return {"status": "healthy", "version": "1.0.0"}
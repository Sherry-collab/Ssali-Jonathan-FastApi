from fastapi import FastAPI
from fastapi.requests import Request

def register_middleware(app: FastAPI):
    
    @app.middleware('http')
    async def custom_loggin(request: Request, call_next):
        pass
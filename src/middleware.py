from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import JSONResponse
import time
import logging

logger = logging.getLogger('uvicorn.access')
logger.disabled = True

def register_middleware(app: FastAPI):
    
    @app.middleware('http')
    async def custom_loggin(request: Request, call_next):
        start_time = time.time()
        
        response = await call_next(request)
        
        processing_time = time.time() - start_time
        
        message = f"{request.client.host}:{request.client.port} - {request.method} - {request.url.path} - {response.status_code} completed after {processing_time}s"
        
        print(message)
        
        return response
    
    @app.middleware(app)
    async def authorization(request: Request, call_next):
        if not "Authorization" in request.headers:
            return JSONResponse(
                content= {
                    "message" : "Not Authenticated",
                    "resolution" : "Please provide the right credentials to proceed"
                }
            )
            
        response = await call_next(request)
        
        return response
    
    
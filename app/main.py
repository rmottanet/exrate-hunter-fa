import os
import sys
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request, Response, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.staticfiles import StaticFiles
import uvicorn

# root to sys_path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/app")

load_dotenv(".env")

from app.config import Config

from app.api.routes import router

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.middleware("http")
async def check_query_params(request: Request, call_next):
    try:
        # checkout param
        if request.query_params:
            raise HTTPException(status_code=422, detail="Esta rota não aceita parâmetros.")
        
        response = await call_next(request)
        return response
        
    except HTTPException as e:
        return Response(content=str(e.detail), status_code=e.status_code)
    

# serve static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# service
app.include_router(router)

# Handler RequestValidationError
@app.exception_handler(RequestValidationError)
async def request_validation_exception_handler(request, exc):
    return JSONResponse(status_code=404, content={"message": "No Endpoint"})

# Handler StarletteHTTPException
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(status_code=exc.status_code, content={"message": exc.detail})

# Handler error 500 (Internal Server Error)
@app.exception_handler(Exception)
async def internal_server_error_handler(request, exc):
    return JSONResponse(status_code=500, content={"message": "Internal Server Error"})


if __name__ == "__main__":
    host = os.getenv("HOST", "localhost")
    port = int(os.getenv("PORT", 8000))
    
    # start FastAPI
    uvicorn.run(app, host=host, port=port)

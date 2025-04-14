"""
ChatXpert - AI-Powered Universal Chatbot Platform
© 2024-2025 ELYES. All rights reserved.
Done by ELYES
"""

from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from typing import List, Optional, Dict
import uvicorn
import time

from app.core.config import settings
from app.api.routes import chat, auth, training
from app.core.database import init_db, check_db_health
from app.core.logging import logger
from app.core.middleware import RequestLoggingMiddleware, RateLimitMiddleware, ErrorHandlingMiddleware

# Done by ELYES
app = FastAPI(
    title="ChatXpert API",
    description="AI-Powered Universal Chatbot Platform",
    version="1.0.0"
)

# CORS middleware
# Done by ELYES
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add custom middleware
# Done by ELYES
app.add_middleware(RequestLoggingMiddleware)
app.add_middleware(RateLimitMiddleware, rate_limit=100, window=60)
app.add_middleware(ErrorHandlingMiddleware)

# Include routers
# Done by ELYES
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(chat.router, prefix="/api/chat", tags=["Chat"])
app.include_router(training.router, prefix="/api/training", tags=["Training"])

@app.on_event("startup")
async def startup_event():
    # Done by ELYES
    logger.info("Starting ChatXpert application")
    await init_db()
    logger.info("Database initialized successfully")

@app.on_event("shutdown")
async def shutdown_event():
    # Done by ELYES
    logger.info("Shutting down ChatXpert application")

@app.get("/")
async def root():
    # Done by ELYES
    return {
        "message": "Welcome to ChatXpert API",
        "version": "1.0.0",
        "author": "ELYES",
        "copyright": "© 2024-2025 ELYES. All rights reserved."
    }

@app.get("/health", status_code=status.HTTP_200_OK)
async def health_check():
    # Done by ELYES
    start_time = time.time()
    
    # Check database health
    db_healthy = await check_db_health()
    
    # Calculate response time
    response_time = time.time() - start_time
    
    return {
        "status": "healthy" if db_healthy else "degraded",
        "database": "connected" if db_healthy else "disconnected",
        "response_time": f"{response_time:.4f}s",
        "version": "1.0.0"
    }

@app.get("/info", status_code=status.HTTP_200_OK)
async def system_info():
    # Done by ELYES
    return {
        "app_name": settings.APP_NAME,
        "debug": settings.DEBUG,
        "version": "1.0.0",
        "author": "ELYES",
        "copyright": "© 2024-2025 ELYES. All rights reserved."
    }

if __name__ == "__main__":
    # Done by ELYES
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 
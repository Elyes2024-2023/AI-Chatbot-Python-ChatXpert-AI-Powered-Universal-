from fastapi import Request, Response
from fastapi.middleware.base import BaseHTTPMiddleware
from starlette.middleware.sessions import SessionMiddleware
import time
import redis
from typing import Optional
import json
from app.core.config import settings
from app.core.logging import logger

class RateLimiter:
    def __init__(self):
        self.redis_client = redis.from_url(settings.REDIS_URL)
        self.rate_limit = 100  # requests per minute
        self.window = 60  # seconds

    async def is_rate_limited(self, key: str) -> bool:
        current = await self.redis_client.get(key)
        if current is None:
            await self.redis_client.setex(key, self.window, 1)
            return False
        if int(current) >= self.rate_limit:
            return True
        await self.redis_client.incr(key)
        return False

class SecurityMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)
        self.rate_limiter = RateLimiter()

    async def dispatch(self, request: Request, call_next):
        # Start timer for request duration
        start_time = time.time()
        
        # Rate limiting
        client_ip = request.client.host
        if await self.rate_limiter.is_rate_limited(f"rate_limit:{client_ip}"):
            logger.warning(f"Rate limit exceeded for IP: {client_ip}")
            return Response(
                content=json.dumps({"detail": "Rate limit exceeded"}),
                status_code=429,
                media_type="application/json"
            )

        # Add security headers
        response = await call_next(request)
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
        response.headers["Content-Security-Policy"] = "default-src 'self'"
        
        # Log request duration
        duration = time.time() - start_time
        logger.info(
            "Request processed",
            path=request.url.path,
            method=request.method,
            duration=f"{duration:.3f}s"
        )
        
        return response 
from typing import Any, Optional
import json
from app.core.database import redis_client
from app.core.logging import logger

class Cache:
    @staticmethod
    async def get(key: str) -> Optional[Any]:
        try:
            data = await redis_client.get(key)
            return json.loads(data) if data else None
        except Exception as e:
            logger.error(f"Cache get error: {str(e)}")
            return None

    @staticmethod
    async def set(key: str, value: Any, ttl: int = 3600) -> bool:
        try:
            await redis_client.setex(
                key,
                ttl,
                json.dumps(value)
            )
            return True
        except Exception as e:
            logger.error(f"Cache set error: {str(e)}")
            return False

    @staticmethod
    async def delete(key: str) -> bool:
        try:
            await redis_client.delete(key)
            return True
        except Exception as e:
            logger.error(f"Cache delete error: {str(e)}")
            return False

    @staticmethod
    async def clear_pattern(pattern: str) -> bool:
        try:
            keys = await redis_client.keys(pattern)
            if keys:
                await redis_client.delete(*keys)
            return True
        except Exception as e:
            logger.error(f"Cache clear pattern error: {str(e)}")
            return False 
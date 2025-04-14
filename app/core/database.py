"""
Database configuration and utilities for ChatXpert
© 2024-2025 ELYES. All rights reserved.
Done by ELYES
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool
from contextlib import contextmanager
import time
from typing import Generator
from motor.motor_asyncio import AsyncIOMotorClient
import redis.asyncio as redis
from app.core.config import settings
from app.core.logging import logger

# PostgreSQL
# Done by ELYES
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    poolclass=QueuePool,
    pool_size=5,
    max_overflow=10,
    pool_timeout=30,
    pool_recycle=1800,
    pool_pre_ping=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# MongoDB
# Done by ELYES
mongodb_client = AsyncIOMotorClient(settings.MONGODB_URL)
mongodb = mongodb_client.get_database()

# Redis
# Done by ELYES
redis_client = redis.from_url(settings.REDIS_URL)

@contextmanager
def get_db() -> Generator:
    # Done by ELYES
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def check_db_health() -> bool:
    # Done by ELYES
    try:
        start_time = time.time()
        db = SessionLocal()
        db.execute("SELECT 1")
        duration = time.time() - start_time
        logger.info(f"Database health check successful. Response time: {duration:.3f}s")
        return True
    except Exception as e:
        logger.error(f"Database health check failed: {str(e)}")
        return False
    finally:
        db.close()

async def init_db():
    # Initialize database connections
    # Done by ELYES
    try:
        # Create PostgreSQL tables
        Base.metadata.create_all(bind=engine)
        logger.info("PostgreSQL tables created successfully")
        
        # Test PostgreSQL connection
        db = SessionLocal()
        db.execute("SELECT 1")
        db.close()
        
        # Test MongoDB connection
        await mongodb_client.admin.command('ping')
        
        # Test Redis connection
        await redis_client.ping()
        
        logger.info("All database connections established successfully")
    except Exception as e:
        logger.error(f"Error connecting to databases: {e}")
        raise e

def get_db():
    # Done by ELYES
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 
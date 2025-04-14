"""
Configuration settings for ChatXpert
© 2024-2025 ELYES. All rights reserved.
Done by ELYES
"""

from pydantic_settings import BaseSettings
from typing import Optional
from functools import lru_cache
import os
from dotenv import load_dotenv

# Done by ELYES
load_dotenv()

class Settings(BaseSettings):
    # Application Settings
    # Done by ELYES
    APP_NAME: str = "ChatXpert"
    DEBUG: bool = False
    API_V1_STR: str = "/api/v1"
    
    # Security Settings
    # Done by ELYES
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    ALGORITHM: str = "HS256"
    
    # Database Settings
    # Done by ELYES
    DATABASE_URL: str
    MONGODB_URL: str = "mongodb://localhost:27017/chatxpert"
    REDIS_URL: str = "redis://localhost:6379/0"
    
    # OpenAI Settings
    # Done by ELYES
    OPENAI_API_KEY: str
    OPENAI_MODEL: str = "gpt-3.5-turbo"
    
    # Logging Settings
    # Done by ELYES
    LOG_LEVEL: str = "INFO"
    
    # CORS
    # Done by ELYES
    BACKEND_CORS_ORIGINS: list = ["*"]
    
    class Config:
        # Done by ELYES
        env_file = ".env"
        case_sensitive = True

@lru_cache()
def get_settings() -> Settings:
    # Done by ELYES
    return Settings()

# Done by ELYES
settings = get_settings() 
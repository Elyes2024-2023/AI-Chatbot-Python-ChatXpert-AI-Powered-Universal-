"""
Logging configuration for ChatXpert
© 2024-2025 ELYES. All rights reserved.
Done by ELYES
"""

import logging
import logging.handlers
import os
from pathlib import Path
from app.core.config import settings

# Done by ELYES
# Create logs directory if it doesn't exist
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)

# Configure logging
# Done by ELYES
def setup_logging():
    # Get log level from settings
    log_level = getattr(logging, settings.LOG_LEVEL.upper(), logging.INFO)
    
    # Create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    
    # Create file handler
    file_handler = logging.handlers.RotatingFileHandler(
        filename=log_dir / "chatxpert.log",
        maxBytes=10485760,  # 10MB
        backupCount=5
    )
    file_handler.setFormatter(formatter)
    
    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(log_level)
    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)
    
    # Create logger for this module
    logger = logging.getLogger("chatxpert")
    logger.setLevel(log_level)
    
    return logger

# Done by ELYES
logger = setup_logging() 
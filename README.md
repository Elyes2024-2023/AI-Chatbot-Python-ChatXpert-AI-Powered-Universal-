# ChatXpert - AI-Powered Universal Chatbot

ChatXpert is a powerful, AI-driven chatbot application built with Python, FastAPI, and OpenAI's GPT models. It provides a flexible and extensible platform for creating intelligent conversational interfaces.

## Features

- 🤖 Powered by OpenAI's GPT models
- 🔒 Secure authentication and authorization
- 📝 Conversation history tracking
- 🔄 Real-time chat capabilities
- 🎨 Modern and responsive UI
- ⚡ Fast and scalable backend
- 🔧 Highly configurable
- 📊 Request logging and performance monitoring
- 🛡️ Rate limiting and error handling
- 🏥 Health check endpoints
- 🐳 Docker and Docker Compose support

## Prerequisites

- Python 3.8+
- PostgreSQL
- MongoDB
- Redis
- OpenAI API key
- Docker and Docker Compose (optional, for containerized deployment)

## Installation

### Option 1: Local Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/chatxpert.git
cd chatxpert
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
```
Edit the `.env` file with your configuration values.

5. Initialize the database:
```bash
alembic upgrade head
```

### Option 2: Docker Deployment

1. Clone the repository:
```bash
git clone https://github.com/yourusername/chatxpert.git
cd chatxpert
```

2. Create a `.env` file with your secrets:
```bash
cp .env.example .env
```
Edit the `.env` file and set at least:
- `SECRET_KEY`: A secure random string
- `OPENAI_API_KEY`: Your OpenAI API key

3. Start the services:
```bash
docker-compose up -d
```

## Running the Application

### Local Development

1. Start the backend server:
```bash
uvicorn app.main:app --reload
```

2. Access the application:
- API documentation: http://localhost:8000/docs
- Web interface: http://localhost:8000

### Docker Deployment

The application will be available at:
- API documentation: http://localhost:8000/docs
- Web interface: http://localhost:8000

## Configuration

The application can be configured through environment variables in the `.env` file:

- `DEBUG`: Enable/disable debug mode
- `APP_NAME`: Application name
- `SECRET_KEY`: Secret key for JWT tokens
- `ACCESS_TOKEN_EXPIRE_MINUTES`: JWT token expiration time
- `ALGORITHM`: JWT algorithm (default: HS256)
- `DATABASE_URL`: PostgreSQL database URL
- `MONGODB_URL`: MongoDB connection URL
- `REDIS_URL`: Redis connection URL
- `OPENAI_API_KEY`: Your OpenAI API key
- `OPENAI_MODEL`: OpenAI model to use
- `LOG_LEVEL`: Logging level

## API Endpoints

- `/`: Root endpoint with welcome message
- `/health`: Health check endpoint
- `/info`: System information endpoint
- `/api/auth/register`: User registration
- `/api/auth/token`: User login
- `/api/chat/send`: Send a chat message
- `/api/chat/history`: Get chat history
- `/api/training/data`: Add training data
- `/api/training/upload`: Upload training file
- `/api/training/train`: Train the model
- `/api/training/status/{job_id}`: Check training status

## Project Structure

```
chatxpert/
├── app/
│   ├── api/
│   │   └── routes/
│   │       ├── auth.py
│   │       ├── chat.py
│   │       └── training.py
│   ├── core/
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── logging.py
│   │   ├── middleware.py
│   │   └── security.py
│   └── main.py
├── logs/
├── alembic/
├── tests/
├── .env
├── .env.example
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

**ELYES**

## Copyright

© 2024-2025 ELYES. All rights reserved. 
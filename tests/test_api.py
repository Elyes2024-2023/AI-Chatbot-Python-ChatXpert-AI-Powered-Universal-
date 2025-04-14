"""
Tests for ChatXpert API
© 2024-2025 ELYES. All rights reserved.
Done by ELYES
"""

import pytest
from fastapi.testclient import TestClient
from app.main import app

# Done by ELYES
client = TestClient(app)

def test_read_root():
    # Done by ELYES
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()
    assert "version" in response.json()
    assert "author" in response.json()
    assert "copyright" in response.json()
    assert response.json()["author"] == "ELYES"
    assert "© 2024-2025 ELYES" in response.json()["copyright"]

def test_health_check():
    # Done by ELYES
    response = client.get("/health")
    assert response.status_code == 200
    assert "status" in response.json()
    assert "database" in response.json()
    assert "response_time" in response.json()
    assert "version" in response.json()

def test_system_info():
    # Done by ELYES
    response = client.get("/info")
    assert response.status_code == 200
    assert "app_name" in response.json()
    assert "debug" in response.json()
    assert "version" in response.json()
    assert "author" in response.json()
    assert "copyright" in response.json()
    assert response.json()["author"] == "ELYES"
    assert "© 2024-2025 ELYES" in response.json()["copyright"]

# Note: These tests require a running database
# Uncomment to run with a test database
"""
def test_register_user():
    # Done by ELYES
    response = client.post(
        "/api/auth/register",
        json={
            "username": "testuser",
            "email": "test@example.com",
            "full_name": "Test User",
            "disabled": False
        },
        params={"password": "testpassword"}
    )
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"
    assert response.json()["email"] == "test@example.com"

def test_login_user():
    # Done by ELYES
    response = client.post(
        "/api/auth/token",
        data={
            "username": "testuser",
            "password": "testpassword"
        }
    )
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"
""" 
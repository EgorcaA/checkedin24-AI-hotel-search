import pytest
import sys
from pathlib import Path

# Add the backend directory to the Python path
backend_dir = str(Path(__file__).parent.parent)
if backend_dir not in sys.path:
    sys.path.append(backend_dir)

from app.main import app
from fastapi.testclient import TestClient

@pytest.fixture
def client():
    return TestClient(app) 
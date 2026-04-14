from copy import deepcopy
from pathlib import Path
import sys

import pytest
from fastapi.testclient import TestClient

PROJECT_SRC = Path(__file__).resolve().parents[1] / "src"
if str(PROJECT_SRC) not in sys.path:
    sys.path.insert(0, str(PROJECT_SRC))

from app import activities, app  # noqa: E402

BASE_ACTIVITIES = deepcopy(activities)


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities() -> None:
    activities.clear()
    activities.update(deepcopy(BASE_ACTIVITIES))
    yield
    activities.clear()
    activities.update(deepcopy(BASE_ACTIVITIES))

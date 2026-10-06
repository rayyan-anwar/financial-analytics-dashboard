import pandas as pd
from fastapi.testclient import TestClient
from backend.app.analytics import analyze
from backend.app.main import app
def test_metrics():
    m=analyze(pd.DataFrame({"close":[100,101,102,101,104,105]}))
    assert m["latest_close"]==105.0 and m["observations"]==6
def test_api():
    assert TestClient(app).get("/health").json()["author"]=="Rayyan Anwar"

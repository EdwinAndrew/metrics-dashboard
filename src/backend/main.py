from fastapi import FastAPI # type: ignore
from typing import List
from datetime import datetime, timedelta
from backend.app.models.schema import Deployment

app = FastAPI(title="Deployment Metrics Dashboard")

def get_mock_deployments() -> List[Deployment]:
    now = datetime.now()
    mock_data = [
        Deployment(
            id=1,
            service_name="user-service",
            environment="production",
            start_time=now - timedelta(minutes=30),
            end_time=now - timedelta(minutes=25),
            status="completed",
            sync_status="Synced",
            health_status="Healthy",
            duration_seconds=300  # 5 minutes
        ),
        Deployment(
            id=2,
            service_name="payment-service",
            environment="staging",
            start_time= now - timedelta(minutes=15),
            end_time=None,
            status="running",
            sync_status="OutOfSync",
            health_status="Progressing",
            duration_seconds=None
        )
    ]
    return mock_data



@app.get("/health")
async def health_check():
    return {"status": "healthy"}


@app.get("/deployments", response_model=List[Deployment])
async def get_deployments():
    return get_mock_deployments()
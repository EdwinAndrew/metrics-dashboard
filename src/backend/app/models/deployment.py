from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class Deployment(BaseModel):
    id: int
    service_name: str
    environment: str
    start_time: datetime
    end_time: Optional[datetime] = None
    status: str
    sync_status: str
    health_status: str
    duration_seconds: Optional[float] = None
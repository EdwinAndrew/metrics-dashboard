from sqlalchemy.orm import DeclarativeBase, mapped_column # type: ignore
from sqlalchemy.types import Integer, String, Float # type: ignore
from sqlalchemy import DateTime # type: ignore

class Base(DeclarativeBase):
    pass

class DeploymentModel(Base):
    __tablename__ = "deployments"
    id = mapped_column(Integer, primary_key=True, index=True)
    service_name = mapped_column(String(255), index=True)
    environment = mapped_column(String(50))
    start_time = mapped_column(DateTime())  # Note the parentheses
    end_time = mapped_column(DateTime(), nullable=True)  # Note the parentheses
    status = mapped_column(String(50))
    sync_status = mapped_column(String(50))
    health_status = mapped_column(String(50))
    duration_seconds = mapped_column(Float, nullable=True)
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base 
from dotenv import load_dotenv
import os

load_dotenv()
database_url = os.getenv("DATABASE_URL")

engine = create_async_engine(database_url, echo=True)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, export_on_commit=False)

async def get_db():
    async with AsyncSessionLocal() as session: 
        try: 
            yield session
        finally:
            await session.close()
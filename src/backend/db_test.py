# src/backend/db_test.py
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text
from dotenv import load_dotenv
import os

async def test_connection():
    # Load environment variables
    load_dotenv()
    
    # Get DATABASE_URL from environment
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        raise ValueError("DATABASE_URL not found in environment variables")
    
    print(f"Attempting to connect to database...")
    
    # Create engine
    engine = create_async_engine(database_url, echo=True)
    
    try:
        # Try to connect
        async with engine.connect() as conn:
            # Execute a simple query
            result = await conn.execute(text("SELECT * FROM metrics_dashboard"))
            print("Connection successful!")
            
            # Fetch the result
            value = result.scalar()
            print(f"Test query result: {value}")
            
    except Exception as e:
        print(f"Error connecting to the database: {e}")
    
    finally:
        # Dispose the engine
        await engine.dispose()

if __name__ == "__main__":
    asyncio.run(test_connection())
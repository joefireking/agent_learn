from typing import AsyncGenerator

from click import echo
from fastapi import Depends,HTTPException,status
from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession,create_async_engine,async_sessionmaker
from jose import JWTError,jwt
from backend.config import get_settings
settings = get_settings()
engine=create_async_engine(
    settings.database_url,
    pool_size=10,
    max_overflow=20,
    echo=False,
)
AsyncSessionLocal=async_sessionmaker(engine,expire_on_commit=False)
async def get_db() ->AsyncGenerator[AsyncSession,None]:
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise

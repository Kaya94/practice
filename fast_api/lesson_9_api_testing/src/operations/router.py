from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert
from database import get_async_session
from operations.models import operation
from operations.schemas import OperationCreate
from fastapi_cache.decorator import cache
from time import time


router = APIRouter(
    prefix="/operations",
    tags=["Operations"]
)


@router.get("/long_operation")
@cache(expire=30)
def get_long_op():
    time.sleep(2)
    return "Много много данных, которые вычислялись сто лет"

@router.get("/")
async  def get_specific_operations(operation_type: str, session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(operation).where(operation.c.type == operation_type)
        result = await session.execute(query)
        return {
            "status": "succes",
            "data": result.all(),
            "details": None
        }
    except Exception:
        raise HTTPException(
            status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })


@router.post("/")
async def post_specific_operations(new_opertion: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(operation).values(**new_opertion.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}

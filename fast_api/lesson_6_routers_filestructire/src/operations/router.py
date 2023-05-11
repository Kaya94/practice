from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert
from database import get_async_session
from operations.models import operation
from operations.schemas import OperationCreate


router = APIRouter(
    prefix="/operations",
    tags=["Operations"]
)


@router.get("/")
async  def get_specific_operations(operation_type: str, session: AsyncSession = Depends(get_async_session)):
    query = select(operation).where(operation.c.type == operation_type)
    result = await session.execute(query)
    return result.all()


@router.post("/")
async def post_specific_operations(new_opertion: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(operation).values(**new_opertion.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}

from fastapi import FastAPI, Depends
from auth.auth import auth_backend
from auth.schemas import UserCreate, UserRead
from fastapi_users import FastAPIUsers
from auth.models import User
from auth.manager import get_user_manager
from operations.router import router as operations_router
from redis import asyncio as aioredis
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from operations.router import router as router_operation
from tasks.router import router as router_tasks
from fastapi.middleware.cors import CORSMiddleware
from pages.router import router as router_pages
from fastapi.staticfiles import StaticFiles


app = FastAPI(
    title="Trading App"
)

# Подключаем статику
app.mount("/static", StaticFiles(directory="static"), name="static")

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)


app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

current_user = fastapi_users.current_user()

@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username}"


@app.get("/unprotected-route")
def unprotected_route():
    return f"Hello, anonym"

# Подключаем роутеры
app.include_router(router_operation)
app.include_router(router_tasks)
app.include_router(router_pages)

# Выбираем адреса сайтов, которые могут общаться с нашим аппи
origins = [
    "http://localhost:3000",
]

# Прописываем методы, доступные для работы с сайтом
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],
)


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://localhost")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")

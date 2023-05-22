from typing import Any
from fastapi import FastAPI, Depends, Request, HTTPException


app = FastAPI()


# yeild
# Отдаем асинхронную сессию для работы в ендпоинте
async def get_async_session():
    print("Получение сессии")
    session = "session"
    yield session
    print("Уничтожение сессии")

# ендпоинт работает с сессией, отдает ответ клиенту и отдает контроль обратно в get_async_session
@app.get("/get_items")
async def get_items(session=Depends(get_async_session)):
    print(session)
    return [{"id": 1}]


# parameters
# Прокинуть параметры которые мы хотим использовать через зависимость

# Создадим функцию с передаваемыми параметрами и отдадим словарь
def pagination_params(limit: int = 10, skip: int = 0):
    return {"limit": limit, "skip": skip}

# Перед тем как выполнять какой то код в функции, fast api прогоняет зависимости.
# Обьект вызываемый в Depends будет: pagintaiont_params = pagination_params()
@app.get("/subjects")
async def get_subjects(pagination_params: dict = Depends(pagination_params)):
    return pagination_params


# class
#
class PaginationParams():
    def __init__(self, limit: int = 10, skip: int = 0) -> None:
        self.limit = limit
        self.skip = skip


@app.get("/subjects")
async def get_subjects(pagination_params: PaginationParams = Depends(PaginationParams)):
    return pagination_params


# dependecies = [Depends(...)]
# class call
# request
# Есть класс который отвечает за аутентификацию пользователя или авторизацию

class AuthGuard():
    
    def __init__(self, name: str) -> None:
        self.name = name

    # Если хотим вызвать экземпляр класса как функцию
    def __call__(self, request: Request) -> Any:
        if "super_coockie" not in request.cookies:
            raise HTTPException(status_code=403, detail="Доступ запрещен")
        # Проверяем что в куках есть инфа о наличии прав пользователя
        return True


auth_guard_payments = AuthGuard("payments")



#создадим ендпоинт, вызовем функцию
# Вынесем зависимость из функции, так как не используем ее и помещаем в декоратор

@app.get("/payments", dependencies= [Depends(auth_guard_payments)])
def get_payments():
    return "my payments..."

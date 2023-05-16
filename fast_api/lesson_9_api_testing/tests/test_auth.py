import pytest
from tests.conftest import client, async_session_maker
from sqlalchemy import insert, select
from src.auth.models import role


# Создаем роль в сессии для регистрации пользователя 'так как работаем с базой данных, функция ассинхронная'
async def test_add_role():
    # открываем новую сессию
    async with async_session_maker() as session:
        # Вставляем в табличку "role" новую строчку
        stmt = insert(role).values(id=1, name="admin", permissions=None)
        # Выполнить с помощью сессии
        await session.execute(stmt)
        # Сделать комит, для отправки данных в бд
        await session.commit()
        
    # Убедиться, что роль добавилась
        # Выбираем все роли
        query = select(role)
        # Исполняем запрос
        result = await session.execute(query)
        # Выводим на печать все данные
        print(result.all())
        
        # Убедимся что "result.all()" равен заданным данным "id=1, name="admin", permissions=None"
        assert result.all() == [(1, 'admin', None)], "Роль не добавилась"
    


# Проверка на регистрацию пользователя
def test_register():
    response = client.post("/auth/register", json={
        "email": "string",
        "password": "string",
        "is_active": True,
        "is_superuser": False,
        "is_verified": False,
        "username": "string",
        "role_id": 1
    })

    # Проверяем что пользователь создан
    assert response.status_code == 201, "Пользователь не зарегестрирован"

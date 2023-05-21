from httpx import AsyncClient

# Тестирование асинхронной функции операции с прокидованим клиента в аргументы "ac",так как является фикстурой
async def test_add_specific_operations(ac: AsyncClient):
    response = await ac.post("/operations", json={
        "id": 1,
        "quantity": "25.5",
        "figi": "figi_CODE",
        "instrument_type": "bond",
        "date": "2023-02-01T00:00:00",
        "type": "Выплата купонов",
    })
    # Проверяем код ответа сервера на добавление операции
    assert response.status_code == 200

async def test_get_specific_operations(ac: AsyncClient):
    response = await ac.get("/operations", params={
        "operation_type": "Выплата купонов",
    })
    # Проверяем статус код
    assert response.status_code == 200
    # Проверяем, что статус в таблице равен "success"
    assert response.json()["status"] == "success"
    # Проверяем, что добавилась одна запись
    assert len(response.json()["data"]) == 1
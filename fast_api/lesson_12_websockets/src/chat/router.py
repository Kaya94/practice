from fastapi import WebSocket, WebSocketDisconnect, APIRouter
from chat.models import Messages
from database import async_session_maker
from sqlalchemy import insert

# Создаем роутер и добавляем его в main.py
router = APIRouter(
    prefix="/chat",
    tags="chat"
)

# Класс хранит в себе активные сокет соединения, для общения с клиентом.
# Если пользователь отключается, то удаляется из списка с сокетами.
class ConnectionManager:
    # При инициализации создается переменная с пустыми соединениями
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    # Функция для подключения нового пользователя. Добавляет его в список
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
    
    # Функция для отключения. Удаляет сокет из списка.
    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    # Функция для отправки персонального сообщения, отдному клиенту
    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    # Функция для отправки всем клиентам. Броадкастинг
    async def broadcast(self, message: str, add_to_db: bool):
        if add_to_db:
            await self.add_messages_to_database(message)
        for connection in self.active_connections:
            await connection.send_text(message)

    # staticmethod превращает метод, определенный внутри класса, в обычную функцию,
    # которая не имеет доступа к экземпляру класса self , поэтому ее можно вызывать без создания экземпляра класса.
    @staticmethod
    # Функция добавляет сообщения в базу данных
    async def add_messages_to_database(message: Messages):
        # Открываем ссесию и добавляем сообщение в бд
        async with async_session_maker() as session:
            stmt = insert(Messages).values(
                message=message
            )
            # Необходимо заекзекьютить
            session.execute(stmt)
            # Сделать комит
            session.commit()

# Создаем экземпляр класса ConnectionManager. Обьявляем менеджера
manager = ConnectionManager()

@router.websocket("/ws/{client_id}")
# Получаем id клиента и добавляем его в список соединений менеджера
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try:
        while True:
            # Ждем сообщение от клиента
            data = await websocket.receive_text()
            await manager.broadcast(f"Client #{client_id} says: {data}", add_to_db=True)
    # При отсоединении пользователя отправляем всем, что клиент покинул чат
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat", add_to_db=False)
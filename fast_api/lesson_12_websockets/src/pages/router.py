from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from operations.router import get_specific_operations

# Создаем роутер
router = APIRouter(
    prefix="/pages",
    tags=["Pages"]
)

# Подключаем шаблоны к Fast API и указываем директорию с шаблоном
templates = Jinja2Templates(directory="templates")

# Пишем базовый роутер
@router.get("/base")
# Обзяталеьно передаем запрос "request"
def get_base_page(request: Request):
    # Рендерим ответ и отдаем requset в наш шаблон
    return templates.TemplateResponse("base.html", {"request": request})

# Роутер для страницы "search", обязательно передать аргумент в качестве параметра пути "operation_type"
@router.get("/search/{operation_type}")
def get_search_page(request: Request, operations=Depends(get_specific_operations)):
    # Передаем запрос и "data", так как задано в структуре "operations.router"
    return templates.TemplateResponse("search.html", {"request": request, "operations": operations["data"]})

# Роутер для страницы "chat"
@router.get("/chat")
# Обзяталеьно передаем запрос "request"
def get_chat_page(request: Request):
    # Рендерим ответ и отдаем requset в наш шаблон
    return templates.TemplateResponse("chat.html", {"request": request})
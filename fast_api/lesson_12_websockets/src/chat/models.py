from sqlalchemy import Column, Integer, String

from src.database import Base


class Messages(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True)
    messages = Column(String)
    
    # Создаем метода для сериализации результата данных SQLalchemy в json, для отправки в Js
    # Получаем данные в формате словаря, для дальнейщего конвертирования в Json
    def as_dict(self):
        return {c.name:  getattr(self, c.name) for c in self.__table__.columns}
    
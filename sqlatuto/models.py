from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class ToDo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    completed = Column(Boolean, default=False)


    def __repr__(self):
        return f'todo item: {self.title}'

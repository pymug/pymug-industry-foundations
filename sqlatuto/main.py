from sqlalchemy import select
from models import ToDo
from database import Base, engine, SessionLocal


Base.metadata.create_all(bind=engine)

def create_todo(title: str):
    with SessionLocal() as session:
        new_todo = ToDo(title=title)
        session.add(new_todo)
        session.commit()
        session.refresh(new_todo)
        return new_todo

def list_todos():
    with SessionLocal() as session:
        stmt = select(ToDo)
        return session.scalars(stmt).all()

def complete_todo(todo_id: int):
    with SessionLocal() as session:
        todo = session.get(ToDo, todo_id)
        if todo:
            todo.completed = True
            session.commit()

def delete_todo(todo_id: int):
    with SessionLocal() as session:
        todo = session.get(ToDo, todo_id)
        if todo:
            session.delete(todo)
            session.commit()

if __name__ == "__main__":
    create_todo("Learn SQLAlchemy 2.0")
    create_todo("Build ToDo App with SQLite")
    create_todo("Build ToDo App with SQLite 2")
    create_todo("Build ToDo App with SQLite 3")

    print("\nAll Todos:")
    for todo in list_todos():
        print(todo)

    complete_todo(1)
    print("\nAfter completing first todo:")
    for todo in list_todos():
        print(todo)

    delete_todo(2)
    print("\nAfter deleting second todo:")
    for todo in list_todos():
        print(todo)

from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from models import ToDo, engine, create_table

app = FastAPI()

@app.get('/')
def crt():
    create_table()

@app.post('/')
def make_model(data: dict):
    with Session(engine) as session:
        deal = ToDo(
            title=data.get("title"),
            description=data.get("description"),
            completed=False,
        )
        session.add(deal)
        session.commit()
        td = session.query(ToDo).get(deal.id)
    return td

@app.get('/todo/{id}')
def extract_todo(id: int):
    with Session(engine) as session:
        todo = session.query(ToDo).get(id)
    if todo:
        return todo
    return HTTPException(status_code=404, detail="Invalid id")

@app.put('/update_todo')
def update(id: int, title: str, description: str, completed=False):
    with Session(engine) as session:
        todo = session.query(ToDo).get(id)
        todo.title = title
        todo.description = description
        todo.completed = completed
        session.commit()
        todo = session.query(ToDo).get(todo.id)
    return todo

@app.delete('del_todo')
def del_todo(id: int):
    with Session(engine) as session:
        todo = session.query(ToDo).get(id)
        if todo:
            session.delete(todo)
            session.commit()
            return True
        return HTTPException(status_code=404, detail="Trying to delete ghost value")






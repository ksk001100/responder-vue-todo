import sys
import time

sys.path.append('..')

from server import api
from server.model import Todo
from server.database import session


class IndexCreateTodo:
    def on_get(self, req, resp):
        todos = session.query(Todo).all()
        session.close()
        resp.media = [{'id': todo.id, 'text': todo.text} for todo in todos]

    async def on_post(self, req, resp):
        @api.background.task
        def create(data):
            try:
                todo = Todo(text=data['text'])
                session.add(todo)
                session.commit()
            except Exception as e:
                print(e)
                session.rollback()
            finally:
                session.close()

        data = await req.media()
        create(data)

        resp.media = {'success': True}


class DeleteTodo:
    async def on_delete(self, req, resp, id):
        @api.background.task
        def delete():
            try:
                todo = session.query(Todo) \
                            .filter(Todo.id == id) \
                            .first()
                session.delete(todo)
                session.commit()
            except Exception as e:
                print(e)
                session.rollback()
            finally:
                session.close()

        delete()

        resp.media = {'success': True}

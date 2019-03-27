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
        def save(data):
            time.sleep(3)
            todo = Todo(text=data['text'])
            session.add(todo)
            session.commit()
            session.close()

        data = await req.media()
        save(data)

        resp.media = {'success': True}


class ShowUpdateDeleteTodo:
    def on_get(self, req, resp, id):
        todo = session.query(Todo) \
                      .filter(Todo.id == id) \
                      .first()
        session.close()
        resp.media = {
            'id': todo.id,
            'text': todo.text
        }

    async def on_put(self, req, resp, id):
        @api.background.task
        def update(data):
            time.sleep(3)
            todo = session.query(Todo) \
                          .filter(Todo.id == id) \
                          .first()
            todo.text = data['text']
            session.commit()
            session.close()

        data = await req.media()
        update(data)

        resp.media = {'success': True}

    async def on_delete(self, req, resp, id):
        @api.background.task
        def drop():
            time.sleep(3)
            todo = session.query(Todo) \
                          .filter(Todo.id == id) \
                          .first()
            session.delete(todo)
            session.commit()
            session.close()

        drop()

        resp.media = {'success': True}

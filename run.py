from server import api
from server.controller import IndexCreateTodo, ShowUpdateDeleteTodo


def routes():
    api.add_route('/', static=True)
    api.add_route('/api/todos', IndexCreateTodo)
    api.add_route('/api/todos/{id}', ShowUpdateDeleteTodo)


if __name__ == '__main__':
    routes()
    api.run()

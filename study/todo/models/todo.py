from copy import copy


class TodoNotFound(Exception):
    pass


class Todo:
    TODOS = []
    NEXT_ID = 0

    def __init__(self, content: str):
        self.id = None
        self.content = content

    def insert(self):
        self.id = Todo.NEXT_ID
        Todo.NEXT_ID += 1
        Todo.TODOS.append(copy(self))
        return self.id

    def update(self):
        todos_idx = [i for i, todo in enumerate(Todo.TODOS) if todo.id == self.id]
        if not todos_idx:
            raise TodoNotFound
        Todo.TODOS[todos_idx[0]] = copy(self)

    def delete(self):
        todos_idx = [i for i, todo in enumerate(Todo.TODOS) if todo.id == self.id]
        if not todos_idx:
            raise TodoNotFound
        del Todo.TODOS[todos_idx[0]]

    @classmethod
    def get_all(cls):
        return Todo.TODOS

    @classmethod
    def get(cls, todo_id: int):
        todos = [todo for todo in Todo.TODOS if todo.id == todo_id]
        if not todos:
            raise TodoNotFound
        return copy(todos[0])
class Stack():

    def __init__(self):
        self.el = []

    def push(self, el):
        self.el.append(el)

    def pop(self):
        return self.el.pop()

    def peek(self):
        return self.el[-1]

    def is_empty(self):
        return self.el == []

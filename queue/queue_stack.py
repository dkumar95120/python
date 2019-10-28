class Queue:
    def __init__(self):
        self.q = []
    def enqueueCharacter(self, ch):
        self.q.append(ch)

    def dequeueCharacter(self):
        if bool(self.q):
            return self.q.pop(0)
        else:
            return -1
    def print(self):
        if bool(self.q):
            print(self.q)

class Stack:
    def __init__(self):
        self.stack = []

    def pushCharacter(self, ch):
        self.stack.append(ch)

    def popCharacter(self):
        if bool(self.stack):
            return self.stack.pop(-1)
        else:
            return -1
    def print(self):
        if bool(self.stack):
            print(self.stack)

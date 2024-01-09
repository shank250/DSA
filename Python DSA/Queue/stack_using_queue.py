# implement stack using queue

from typing import List
from queue import Queue

class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def getSize(self) -> int:
        return self.q1.qsize()

    def isEmpty(self) -> bool:
        return self.getSize() == 0

    def push(self, element: int) -> None:
        while not self.q1.empty():
            self.q2.put(self.q1.get())

        self.q1.put(element)

        while not self.q2.empty():
            self.q1.put(self.q2.get())

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        return self.q1.get()

    def top(self) -> int:
        if self.isEmpty():
            return -1
        return self.q1.queue[0]
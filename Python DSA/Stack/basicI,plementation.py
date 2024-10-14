# from sys import *
# from collections import *
# from math import *
# from typing import List

class Stack:
    def __init__(self, n: int):
        self.size = n
        self.topPtr = 0
        self.stack = [0]*self.size

    def push(self, num: int):
        if self.size == self.topPtr:
            return
        else:
            self.stack[self.topPtr] = num
            self.topPtr += 1

    def pop(self) -> int:
        if self.topPtr == 0:
            return -1
        num = self.stack[self.topPtr - 1]
        self.stack.pop(self.topPtr - 1)
        self.topPtr -= 1
        return num

    def top(self) -> int:
        if self.topPtr == 0:
            return -1
        else:
            rtn = self.stack[self.topPtr - 1]
            return rtn

    def isEmpty(self) -> int:
        return self.topPtr == 0

    def isFull(self) -> int:
        return self.topPtr == self.size


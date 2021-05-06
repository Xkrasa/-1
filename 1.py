class SeqQueue(object):
    def __init__(self,max):
        self.max = max
        self.front = 0
        self.rear = 0
        self.data = [None for i in range(self.max)]
class CircleQueue(object):
    def __init__(self,max):
        self.max = max
        self.data = [None for i in range(self.max)]
        self.front = 0
        self.rear = 0\

    def empty(self):
        return self.front == self.rear

    def push(self, val):
        # 如果队列满了，抛出异常
        if (self.rear + 1) % self.max == self.front:
            raise IndexError("队列为满")
        # 在队尾插入新的关键字
        self.data[self.rear] = val
        # 修改队尾指针
        self.rear = (self.rear + 1) % self.max

    def pop(self):
        # 如果队列为空，抛出异常
        if self.empty():
            raise IndexError("队列为空")
        # 队列不为空，获取队首元素
        cur = self.data[self.front]
        # 修改队首指针，指向下一个位置
        self.front = (self.front + 1) % self.max
        # 返回原队首元素
        return cur

    def peek(self):
        if self.empty():
            raise IndexError("队列为空")
        # 返回队首元素
        return self.data[self.front]
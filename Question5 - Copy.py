class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.queue:
            return "Queue is empty"
        return self.queue.pop(0)

    def front(self):
        if not self.queue:
            return "Queue is empty"
        return self.queue[0]

    def display(self): #Function to display the queue
        print("Queue:", self.queue)

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.display()
print("Dequeued:", q.dequeue())
q.display()
print("Front:", q.front())

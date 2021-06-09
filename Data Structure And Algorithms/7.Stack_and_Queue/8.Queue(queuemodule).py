from queue import Queue
fQueue=Queue(maxsize=4)
print(fQueue.empty())
fQueue.put(1)
fQueue.put(3)
fQueue.put(3)
fQueue.put(4)
print(fQueue.get())
print(fQueue.qsize())

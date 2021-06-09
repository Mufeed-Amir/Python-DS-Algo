from multiprocessing import Queue
a=Queue(maxsize=3)
a.put(1)
a.put(2)
a.put(3)
print(a.qsize())
print(a.get())
print(a.qsize())

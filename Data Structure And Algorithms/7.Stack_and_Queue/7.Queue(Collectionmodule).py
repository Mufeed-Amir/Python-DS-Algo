from collections import deque

firstdeque=deque(maxlen=3)
firstdeque.append(1)
firstdeque.append(12)
firstdeque.append(16)
k=firstdeque.popleft()
print(k)
print(firstdeque)
firstdeque.clear()
print(firstdeque)
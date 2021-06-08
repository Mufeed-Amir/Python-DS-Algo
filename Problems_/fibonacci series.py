def fibonacci(n):
     ar=[0,1]
     for i in range(0,n-2):
          k=ar[i] + ar[i+1]
          ar.append(k)
     
     return ar

print(fibonacci(100))
def f(n):
     if n==2:
          return 1
     if n==1:
          return 0

     return f(n-1) + f(n-2)
print(f(1))
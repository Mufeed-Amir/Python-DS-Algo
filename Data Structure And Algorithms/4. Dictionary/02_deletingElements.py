a={"one":"uno",
     "two": "dos",
     "three": "tres",
     "four" : 4,
      "five" : 5}

#pop()
b=a.pop("two")
print(b,a)

#popitem()  delete random and returns key and value pair
c=a.popitem()
print(c,a)

#clear()     delete all elements from the list
a.clear()
print(a)

a["mufeed"]="amir"
#del method
del a["mufeed"]
print(a)


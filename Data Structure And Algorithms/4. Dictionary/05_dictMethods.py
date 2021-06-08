a={"one":"uno",
     "two": "dos",
     "three": "tres",
     "four" : 4,
      "five" : 5}

#copy()
dict=a.copy()

#fromkeys() method
#dict.fromkeys(sequence[],value)
new={}.fromkeys([1,2,3,4,5,6],0)
print(new)

#get() method / dict.get(key,value) ##returns the "value" if key doesn't not found
b=a.get("four","The value doesn't found")
print(b)

#item() method / returns the list of key value pair
print(a.items())

#keys() method #
#values() method
print(a.keys())
print(a.values())

#setdefault() method / if key doesn't exit it will add
g=a.setdefault("two2",100)
print(g)
print(a)

#pop() method / dict.pop(key,value) returns "value" if doesn't exist

#update() method
k={"key1": 1, "key2": 2}
a.update(k)
print(a)


a={"one":"uno",
     "two": "dos",
     "three": "tres",
     "four" : 4,
      "five" : 5}


#in operator  / keys only
print("one" in a)

#for loop 

#all()

b={1:True, 2: True, 3:True , 4: True}
all(b)
 
 #any()
c={1:False, 2:False , 3:False , 4: False}
print(any(a))


#len()
print(len(a))


#sorted() / sorted(iterable, reverse, key) reverse=False(default)
myDict={"ep": 1, "au":2, "ueud":0, "msdjd":5}
print(sorted(myDict,key=len))


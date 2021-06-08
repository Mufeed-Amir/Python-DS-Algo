a={"one":"uno",
     "two": "dos",
     "three": "tres",
     "four" : 4,
      "five" : 5}

def traverseDict(dict):
     for key in a:
          print(key,a[key])
     
def searchDict(dt,x):
	for i in dt:
		if dt[i]==x:
			return (f"The value is at the key: {i}")
	return ("The value doesn't exit!!")

print(searchDict(a, "uno"))
	

	
               



           


def _per(arr1,arr2):
     s1=set(arr1)
     s2=set(arr2)
     if s1==s2:
          return True
     else:
          return False


print(_per([1,2,3,4,5],[2,3,4,5,1]))

arr=[2,3,4,4,5,5,6,6,7,7,7]
# a=dict()
# for i in arr:
#      if i in a:
#           a[i]=a[i]+1
#      else:
#           a[i]=1

a={}
for i in range(0,len(arr)):
     if arr[i] in a:
          a[arr[i]].append(i)
     else:
          a[arr[i]]=[i]

print(a[2][0])
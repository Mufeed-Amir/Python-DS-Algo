a=[1,2,3,4]
b=[55,6,7,7,8,]
c=a+b       ###concatenation of lists "+"
print(c)
d=a*2    ##elements are repeated
print(d)

#len()   returns no. of elements
#max()    returns the max no. in the list
#min()    returns the min no. in the list
#sum()    returns the sum of elements in the list 

# t=0
# c=0
# while True:
#      i=input("Enter the No. :")
#      if i=="done":
#           break
#      i=float(i)
#      t +=i
#      c +=1
#      avg=t/c

# print(f"The average of the no.s is : {avg}")
a=[]
while True:
     i=input("Enter the Number: ")
     if i=="done":
          break
     i=int(i)
     a.append(i)

s=sum(a)
l=len(a)
print("The average of the Numbers is:",s/l)
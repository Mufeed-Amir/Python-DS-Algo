##Find the Days above Average Temperature

T=int(input("How many day's temperature? :"))
s=[]
for i in range(1,T+1):
     inp=float(input(f"Day {i}'s high temp: "))
     s.append(inp)
avg=round(sum(s)/T,2)
print("Average  is: ",avg)
m=0
for i in s:
     if i>avg:
          m +=1

print(f"{m} day(s) above average.")


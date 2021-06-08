def lcm(a,b):
     if a>=b:
          c=a
     else:
          c=b
     result=1
     i=2
     while i<(c+1) :
          if a==b==1:
               break
          if a%i==0 or b%i==0:
               if a%i==0 and b%i==0:
                    a=a//i
                    b=b//i
               elif a%i==0:
                    a=a//i
               elif b%i==0:
                    b=b//i
               result=i*result
          else:
               i=i+1
     print(result)

print("mufeed")
lcm(81,18)
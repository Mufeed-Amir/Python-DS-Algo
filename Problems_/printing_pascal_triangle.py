def pT(n):
     a1=[1]
     a2=[1,1]
     an=[1 for i in range(0,n+1)]
     for i in range(0,n):
          an[i+1]=an[i]+an[i+1]

     print(an)

pT(5)


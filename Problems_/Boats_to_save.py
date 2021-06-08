def BoatsToSave(nums,limit):
     nums.sort()
     i=0
     j=len(nums)-1
     count=0
     while i<j:
          if nums[i]+nums[j]<=limit:
               i=i+1
               j=j-1
               count +=1
          elif nums[i]+nums[j]>limit:
               if nums[i]==nums[j]==limit:
                    i=i+1
                    j=j-1
                    count=count+2
               elif nums[j]==limit:
                    j=j-1
                    count=count+1
               elif nums[i]==limit:
                    i=i+1
                    count=count+1
               else:
                    j=j-1
                    count=count+1
                                        
     if i==j:
          return count+1
     else:
          return count


nums=[2,2,2,2]
limit=3
print(BoatsToSave(nums, limit))
# def moveZeroes(nums):
#      l=len(nums)
#      for i in nums:
#           if i==0:
#                nums.remove(0)
#                nums.append(0)
#      return nums


# print(moveZeroes([1,2,3,0,4,56,7,0,566]))


def moveZeroes(nums):
     j=0
     for i in nums:
          if i!=0:
               nums[j]=i
          
               j +=1
     for i in range(j,len(nums)):
          nums[i]=0

     return nums


print(moveZeroes([1,2,3,0,4,5,0,6,7,0,566]))

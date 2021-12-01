nums=["-2"]

while nums[-1]!=-1:
    nums.append(int(input()))

nums=nums[1:len(nums)-1]
count=0
curr=nums[0]+nums[1]+nums[2]
prev=10000000000

for i in range(2, len(nums)):
    curr=nums[i-2]+nums[i-1]+nums[i]

    if curr>prev:
        count+=1

    prev=curr

    
print(count)
    

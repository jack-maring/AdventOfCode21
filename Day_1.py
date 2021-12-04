nums=[int(i) for i in open('Inputs/Day_1.txt', 'r').read().split('\n')]

count=0
curr=nums[0]+nums[1]+nums[2]
prev=curr

for i in range(3, len(nums)):
    curr+=nums[i]-nums[i-3]

    if curr>prev:
        count+=1

    prev=curr
    
print(count)
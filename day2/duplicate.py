nums=[3,6,3,8,5,6,9]
for num in nums:
    if nums.count(num)>1:
        nums[nums.index(num)]=None
while None in nums:
    nums.remove(None)
print(nums)
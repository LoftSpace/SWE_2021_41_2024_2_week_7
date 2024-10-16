from typing import List

def twoSum(nums: List[int],target: int) -> list[int]:
    ans = []
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                ans.append(i)
                ans.append(j)
                return ans
    return 0


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            comp = target - nums[i]
            if comp in nums:
                comp_ind = nums.index(comp)
                if i < comp_ind:
                    return [i, comp_ind]
                elif i > comp_ind:
                    return [comp_ind, i]
                else:
                    continue
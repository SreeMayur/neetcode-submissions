class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        result = 0
        for num in num_set:
            if (num-1) not in num_set:
                current = num
                count = 1
                while (current+1) in num_set:
                    current += 1
                    count += 1
                result = max(result, count)
        return result
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        duplicated_i = set()
        seen_pairs = {}
        for i, val1 in enumerate(nums):
            if val1 in duplicated_i:
                continue
            duplicated_i.add(val1)
            for j, val2 in enumerate(nums[i + 1:]):
                complement = -val1 - val2                
                if complement in seen_pairs and seen_pairs[complement] == i:
                    res.add(tuple(sorted((val1, val2, complement))))
                seen_pairs[val2] = i
        return [list(triplet) for triplet in res]


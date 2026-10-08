class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lft = 0
        rgt = len(numbers)-1
        while lft < rgt:
            total = numbers[lft] + numbers[rgt]
            if total == target:
                return [lft+1, rgt+1]
            elif total > target:
                rgt -= 1
            elif total < target:
                lft += 1
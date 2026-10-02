class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = Counter(nums)
        return [item[0] for item in freq_dict.most_common(k)]
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        n = len(nums)
        print(count)
        for num, freq in count.items():
            print(num)
            print(freq)
            print(n//2)
            if freq > n//2:
                return num
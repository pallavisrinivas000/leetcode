class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write_index = 2  # Start from index 2, as the first two elements can always stay

        for i in range(2, len(nums)):
            if nums[i] != nums[write_index - 2]:
                nums[write_index] = nums[i]
                write_index += 1

        return write_index
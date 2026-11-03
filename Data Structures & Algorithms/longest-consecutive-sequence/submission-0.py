class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # TIME: O(n log n)  because of sorting
        # SPACE: O(1) or O(n) depending on the sort() algorithm being used
        
        if not nums:
            return 0

        nums.sort()
        max_streak = 0
        
        curr_val, curr_streak = nums[0], 0
        i = 0
        while i < len(nums):
            if curr_val != nums[i]:
                curr_val, curr_streak = nums[i], 0
            while i < len(nums) and nums[i] == curr_val:
                i += 1
            curr_streak += 1
            curr_val +=1 
            max_streak = max(max_streak, curr_streak)

        return max_streak
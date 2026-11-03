class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # TIME: O(n)
        # SPACE: O(n)

        hash_set = set(nums)
        res = 0

        for n in hash_set:
            if (n - 1) not in hash_set:
                curr_len = 1
                while n + curr_len in hash_set:
                    curr_len += 1
                res = max(res, curr_len)

        return res
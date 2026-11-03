class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []

        sum = 0

        for n in nums:
            sum += n
            self.prefix.append(sum)
        
        print(self.prefix)

    def sumRange(self, left: int, right: int) -> int:
        while left <= right and left > 0:
            return self.prefix[right] - self.prefix[left - 1]
        return self.prefix[right]




# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
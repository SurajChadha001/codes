class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        sum=0
        while val in nums:
            nums.remove(val)
        nums

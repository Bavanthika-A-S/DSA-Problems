class Solution:
    def singleNumber(self,nums):
        e=0
        for i in nums:
            e=e^i
        return e
        
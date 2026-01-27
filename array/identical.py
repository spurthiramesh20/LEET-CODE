class Solution(object):
    def numIdenticalPairs(self, nums):
        count = {}
        pairs = 0

        for n in nums:
            pairs += count.get(n, 0)
            count[n] = count.get(n, 0) + 1

        return pairs

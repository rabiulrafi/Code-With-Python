class Solution:
    def twoSum(self, nums, target):
        container = {}
        for i, num in enumerate(nums):
            if target - num in container:
                print([container[target - num], i])
                return [container[target - num], i]
            container[num] = i
            print(container)
        return
a = Solution()
a.twoSum([2,2,2,11,2,7,11,15],9)

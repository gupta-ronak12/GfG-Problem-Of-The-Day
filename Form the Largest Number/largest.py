class Solution:
    def findLargest(self, arr):
        nums = list(map(str, arr))
        n = len(nums)

        for i in range(n):
            for j in range(0, n - i - 1):
                if nums[j] + nums[j + 1] < nums[j + 1] + nums[j]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    
        if nums[0] == "0":
            return "0"

        return "".join(nums)
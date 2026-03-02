class Solution:
    def maxWater(self, arr):
        n = len(arr)
        if n <= 2:
            return 0

        left = 1
        right = n - 2

        lMax = arr[0]
        rMax = arr[n - 1]

        res = 0

        while left <= right:
            if rMax <= lMax:
                res += max(0, rMax - arr[right])
                rMax = max(rMax, arr[right])
                right -= 1
            else:
                res += max(0, lMax - arr[left])
                lMax = max(lMax, arr[left])
                left += 1

        return res
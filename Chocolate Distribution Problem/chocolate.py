class Solution:

    def findMinDiff(self, arr,M):
        arr.sort()

        n = len(arr)
        
        if M > n:
            return -1

        min_diff = float('inf')
        
        for i in range(n - M + 1):
            diff = arr[i + M - 1] - arr[i]

            if diff < min_diff:
                min_diff = diff

        return min_diff
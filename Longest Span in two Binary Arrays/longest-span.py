class Solution:
    def equalSumSpan(self, a1, a2):
        # code here
        n = len(a1)
        maxLen = 0

        # Array to store first occurrence of difference
        diff = [-1] * (2 * n + 1)

        prefixSum1 = 0
        prefixSum2 = 0

        for i in range(n):
            prefixSum1 += a1[i]
            prefixSum2 += a2[i]

            currentDiff = prefixSum1 - prefixSum2
            index = currentDiff + n   # shift to avoid negative index

            # If sums are equal from 0 to i
            if currentDiff == 0:
                maxLen = i + 1

            # If difference seen before
            elif diff[index] != -1:
                maxLen = max(maxLen, i - diff[index])

            else:
                diff[index] = i

        return maxLen
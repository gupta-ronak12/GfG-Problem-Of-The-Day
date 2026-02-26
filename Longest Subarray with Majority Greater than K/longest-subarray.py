class Solution:
    def longestSubarray(self, arr, k):
        # Code Here
        n = len(arr)
        first_occurrence = [-1] * (2 * n + 1)
        
        prefix = 0
        ans = 0
        
        for i in range(n):
            if arr[i] > k:
                prefix += 1
            else:
                prefix -= 1
            
            index = prefix + n
            
            if prefix > 0:
                ans = i + 1
            else:
                prev_index = prefix - 1 + n
                if 0 <= prev_index < len(first_occurrence) and first_occurrence[prev_index] != -1:
                    ans = max(ans, i - first_occurrence[prev_index])
            if first_occurrence[index] == -1:
                first_occurrence[index] = i
        
        return ans
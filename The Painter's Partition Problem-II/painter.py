class Solution:
    def minTime (self, arr, k):
        low = max(arr)
        high = sum(arr)
        
        while low < high:
            mid = (low + high) // 2
            
            painters = 1
            curr_sum = 0
            
            for board in arr:
                if curr_sum + board > mid:
                    painters += 1
                    curr_sum = board
                else:
                    curr_sum += board
                    
            if painters <= k:
                high = mid
            else:
                low = mid + 1
                
        return low
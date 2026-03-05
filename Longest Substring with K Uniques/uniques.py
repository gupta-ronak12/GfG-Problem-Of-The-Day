class Solution:
    def longestKSubstr(self, s, k):
        n = len(s)
        
        i = 0
        j = 0
        cnt = 0
        maxi = -1
        
        fre = [0] * 26
        
        while j < n:
            
            idx = ord(s[j]) - ord('a')
            fre[idx] += 1
            
            if fre[idx] == 1:
                cnt += 1
            
            while cnt > k:
                left = ord(s[i]) - ord('a')
                fre[left] -= 1
                
                if fre[left] == 0:
                    cnt -= 1
                
                i += 1
            
            if cnt == k:
                maxi = max(maxi, j - i + 1)
            
            j += 1
        
        return maxi
class Solution:
    def minWindow(self, s, p):
        len1 = len(s)
        len2 = len(p)

        if len1 < len2:
            return ""

        countP = [0] * 256
        countS = [0] * 256
        for ch in p:
            countP[ord(ch)] += 1

        start = 0
        startIdx = -1
        minLen = float('inf')
        count = 0

        for j in range(len1):
            countS[ord(s[j])] += 1

            if countP[ord(s[j])] != 0 and countS[ord(s[j])] <= countP[ord(s[j])]:
                count += 1

            if count == len2:

                while (countS[ord(s[start])] > countP[ord(s[start])] or 
                       countP[ord(s[start])] == 0):

                    if countS[ord(s[start])] > countP[ord(s[start])]:
                        countS[ord(s[start])] -= 1

                    start += 1

                length = j - start + 1

                if minLen > length:
                    minLen = length
                    startIdx = start

        if startIdx == -1:
            return ""

        return s[startIdx:startIdx + minLen]
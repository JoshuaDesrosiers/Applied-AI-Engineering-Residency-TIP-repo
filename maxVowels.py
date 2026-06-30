class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vow = set("aeiou")
        [sum,maxSum] = [0,0]
        sub = 0
        first = s[0]
        index = -1
        for char in s:
            index += 1
            sub+=1
            if char in vow: sum+=1
            if sub < k: continue
            if sub > k:
                if first in vow: sum-=1
                first = s[index-k+1]
            if sum>maxSum:
                maxSum = sum
        return maxSum


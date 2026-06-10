# Day 3

Problem: 
leetcode link:

```js
function reverseString(s) {
  let left = 0;
  let right = s.length - 1;
  while (left < right) {
    let temp = s[left];
    s[left] = s[right];
    s[right] = temp;
    left++;
    right--;
  }
  return s;
}
```
Input:

Output:

Algorith:


Python Solution:

```py
def reverseString(s):
  s.reverse()

def lengthOfLongestSubstring(self, s: str) -> int:
    seen = {}
    left = 0
    maxLength = 0
    for right in range(len(s)):
        try:
            if seen[s[right]] >= left:
                left = seen[s[right]] + 1
        except:''
        seen[s[right]] = right
        maxLength = max(maxLength, right - left + 1)
    
    return maxLength
        
```

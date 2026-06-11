# Day 4

Problem: 
leetcode link:

```js
function containsDuplicate(nums) {
  const seen = new Set();
  for (let i = 0; i < nums.length; i++) {
    if (seen.has(nums[i])) {
      return true;
    }
    seen.add(nums[i]);
  }
  return false;
}

function groupAnagrams(strs) {
  const map = {};
  for (let i = 0; i < strs.length; i++) {
    const key = strs[i].split('').sort().join('');
    if (map[key] === undefined) {
      map[key] = [];
    }
    map[key].push(strs[i]);
  }
  return Object.values(map);
}
```
Input:

Output:

Algorith:


Python Solution:

```py
# solution here

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numSet = set(nums)
        return len(numSet) != len(nums)


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for i in strs:
            key = ''.join(sorted(i))
            try:map[key]
            except:map[key] = []
            map[key].append(i)
        return list(map.values())

```

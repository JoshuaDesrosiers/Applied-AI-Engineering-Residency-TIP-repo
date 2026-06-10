# Day 2

Problem: 
leetcode link:

```js
function twoSum(nums, target) {
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] + nums[j] === target) {
        return [i, j];
      }
    }
  }
}

function maxProfit(prices) {
  let minPrice = Infinity;
  let maxProfit = 0;
  for (let i = 0; i < prices.length; i++) {
    if (prices[i] < minPrice) {
      minPrice = prices[i];
    } else if (prices[i] - minPrice > maxProfit) {
      maxProfit = prices[i] - minPrice;
    }
  }
  return maxProfit;
}
```
Input:

Output:

Algorith:


Python Solution:

```py
def twoSum(self, nums: List[int], target: int) -> List[int]:
    for x in range(len(nums)):
        for y in range(len(nums)-(x+1)):
            if (nums[x] + nums[(x+1) + y]) == target:
                return [x,(x+1)+y]
        
def maxProfit(self, prices: List[int]) -> int:
    minPrice = math.inf
    maxProfit = 0
    for i in range(len(prices)):
        if prices[i] < minPrice: minPrice = prices[i]
        elif prices[i] - minPrice > maxProfit: maxProfit = prices[i] - minPrice
    return maxProfit
```

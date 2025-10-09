# Partition Equal Subset Sum

## Problem Description

Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets with equal sum.

## Examples

### Example 1:

```
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
```

### Example 2:

```
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
```

## Constraints

- 1 <= nums.length <= 200
- 1 <= nums[i] <= 100

## Desired Time Complexity

- **Time Complexity**: O(n \* sum)
- **Space Complexity**: O(sum)

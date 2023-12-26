#Find the duplicate number in an array of integers

"""
Restrictions:
- You must not modify the array.
- You must use only constant, O(1) extra space.
- Your runtime complexity should be less than O(n^2).
"""

# Using the Floyd's Tortoise and Hare (Cycle Detection) algorithm

def findDuplicateNumber(nums):
  tortoise = nums[0]
  hare = nums[0]

  while True:
    tortoise = nums[tortoise]
    hare = nums[nums[hare]]
    if tortoise == hare:
        break

  tortoise = nums[0]
  while tortoise != hare:
    tortoise = nums[tortoise]
    hare = nums[hare]

  return tortoise

nums = [3, 1, 3, 4, 2]
print("The array is: ", nums)
print("The duplicate number is: ", findDuplicateNumber(nums))

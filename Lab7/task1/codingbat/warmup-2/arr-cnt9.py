def array_count9(nums):
  count = 0
  for element in nums:
    if element == 9:
      count += 1
  return count
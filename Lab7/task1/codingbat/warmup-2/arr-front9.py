def array_front9(nums):
  for element in nums[:4]:
    if element == 9:
      return True
  return False
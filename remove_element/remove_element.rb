def remove_element(nums, val)
  left_pointer = 0
  right_pointer = nums.length - 1
  counter = 0

  while left_pointer < right_pointer
    left = nums[left_pointer]
    right = nums[right_pointer]

    if right == val
      counter += 1
      nums[right_pointer] = '-'
      right_pointer -= 1
      next
    end

    if left != val
      left_pointer += 1
      next
    end

    nums[left_pointer] = nums[right_pointer]
    nums[right_pointer] = '-'
    left_pointer += 1
    right_pointer -= 1
    counter += 1
  end

  nums.length - counter
end

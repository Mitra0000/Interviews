def merge_sort(array):
    if len(array) > 1:
        # Split.
        middle = len(array) // 2
        left = array[:middle]
        right = array[middle:]
        merge_sort(left)
        merge_sort(right)

        # Merge
        left_pointer = 0
        right_pointer = 0
        idx = 0
        while left_pointer < len(left) and right_pointer < len(right):
            if left[left_pointer] <= right[right_pointer]:
                array[idx] = left[left_pointer]
                left_pointer += 1
            else:
                array[idx] = right[right_pointer]
                right_pointer += 1
            idx += 1

        while left_pointer < len(left):
            array[idx] = left[left_pointer]
            left_pointer += 1
            idx += 1
        
        while right_pointer < len(right):
            array[idx] = right[right_pointer]
            right_pointer += 1
            idx += 1

if __name__ == "__main__":
    nums = [11, 4, 0, 16, 3, 5, 8, 12, 7, 18, 17, 14, 10, 13, 2, 15, 1, 9, 6]
    print(nums)
    merge_sort(nums)
    print(nums)
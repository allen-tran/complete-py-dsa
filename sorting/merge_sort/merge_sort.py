def merge_sort(nums):
    if len(nums) > 1:
        left_arr = nums[:len(nums)//2]
        right_arr = nums[len(nums)//2:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        l = r = i = 0

        while l < len(left_arr) and r < len(right_arr):
            if left_arr[l] < right_arr[r]:
                nums[i] = left_arr[l]
                i += 1
                l += 1
            else:
                nums[i] = right_arr[r]
                i += 1
                r += 1

        while l < len(left_arr):
            nums[i] = left_arr[l]
            i += 1
            l += 1

        while r < len(right_arr):
            nums[i] = right_arr[r]
            r += 1
            i += 1
    return nums


print(merge_sort([1, 5, 3, 6, 2, 4, 6, 7]))

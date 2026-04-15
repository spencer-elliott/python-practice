#
# Leetcode #4: Median of Two Sorted Arrays
#

def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
        
        # Merge the arrays
        nums = nums1 + nums2

        # Sort in ascending order
        nums.sort()

        # If even amount of numbers, median is average of the middle two
        if len(nums) % 2 == 0:
            high = int(len(nums) / 2)
            low = int(high - 1)
            return (nums[high] + nums[low]) / 2
        # If odd amount of numbers, median is in the middle
        else:
            median = int((len(nums) + 1) / 2)
            return nums[median-1]


# Test case 1
print(findMedianSortedArrays([1,3],[2])) # 2

# Test case 2
print(findMedianSortedArrays([1,2],[3,4])) # 2.5

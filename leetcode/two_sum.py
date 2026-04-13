#
# LeetCode #1: Two Sum
#

def two_sum(nums: list[int], target: int) -> list[int]:

        # Create a dictionary
        num_map = {}

        # Go through the list, enumerate gives us both index and number
        for i, num in enumerate(nums):

            # Calculate necessary complement
            complement = target - num

            # If the complement is a number we have stored, return this pair
            if complement in num_map:
                return[num_map[complement], i]

            # Otherwise, add this number to the map
            num_map[num] = i

# Test cases
print(two_sum([2,7,11,15], 9))  # [0,1]
print(two_sum([3,2,4], 6))  # [1,2]
print(two_sum([3,3], 6))  # [0,1]
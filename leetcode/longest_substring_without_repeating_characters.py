#
# Leetcode #3: Longest Substring Without Repeating Characters
#

def lengthOfLongestSubstring(s: str) -> int:
        
        # Create a window of unique characters
        seen = set()
        left = 0
        length = 0

        # Slide this window across the string
        for right in range(len(s)):
            # If next character is in our window, remove from the left until it is not
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            # If next character is unique, add it to the window
            else:
                seen.add(s[right])
                # Keep track of max length the window reaches.
                length = max(length, right-left+1)
        return length


# Test case 1
print(lengthOfLongestSubstring("abcabcbb")) # 3

# Test case 2
print(lengthOfLongestSubstring("bbbbb")) # 1

# Test case 3
print(lengthOfLongestSubstring("pwwkew")) # 3

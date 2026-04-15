#
# Leetcode #5: Longest Palindromic Substring
#

def longestPalindrome(s: str) -> str:

        best = ""

        # Function that starts at a character and finds the longest palindrome expanding from it
        def expand(left,right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]

        # Try to expand from each character
        for i in range(len(s)):
            # Odd-length palindromes have one character as the center
            palindrome_odd = expand(i,i)
            # Even-length palindromes have two characters as the center
            palindrome_even = expand(i,i+1)

            # Keep track of the longest palindrome found
            if len(palindrome_odd) > len(best):
                best = palindrome_odd
            if len(palindrome_even) > len(best):
                best = palindrome_even
    
        return best


# Test case 1
print(longestPalindrome("babad")) # "bab"

# Test case 2
print(longestPalindrome("cbbd")) # "bb"

#
# Leetcode #7: Reverse Integer
# https://leetcode.com/problems/reverse-integer/
#

def reverse(x: int) -> int:

    # Convert to string
    s = str(x)

    # Reverse the string. If negative, remove the symbol and re-add after
    if s[0] == "-":
        s = s[1:]
        s = s[::-1]
        s = "-" + s
    else:
        s = s[::-1]

    # Convert back into int
    x = int(s)

    # Return number unless outside the integer range - then return 0
    if x > 2**31 - 1 or x < -2**31:
        return 0
    else:
        return x
    

# Test case 1
print(reverse(123)) # 321

# Test case 2
print(reverse(-123)) # -321

# Test case 3
print(reverse(120)) # 21

#
# Leetcode #6: Zigzag Conversion
# https://leetcode.com/problems/zigzag-conversion/
#

def convert(s: str, numRows: int) -> str:

    # If only 1 row, just return the string as-is    
    if numRows == 1:
        return s

    # Create an array to hold each row
    rows = [""] * numRows

    # Track the next row to add to, and whether ascending or descending between rows
    row_tracker = 0
    ascending = True

    for char in s:
        # Add a character to each row, then reverse, repeating in a zigzag pattern
        rows[row_tracker] += char
        if ascending == True:
            row_tracker += 1
            if row_tracker == numRows-1:
                ascending = False
        else:
            row_tracker -= 1
            if row_tracker == 0:
                ascending = True

    # Join the rows as the converted string and return it  
    return "".join(rows)

# Test case 1
print(convert("PAYPALISHIRING", 3)) # "PAHNAPLSIIGYIR"

# Test case 2
print(convert("PAYPALISHIRING", 4)) # "PINALSIGYAHRPI"

# Test case 3
print(convert("A", 1)) # "A"

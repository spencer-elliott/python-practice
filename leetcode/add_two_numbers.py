#
# Leetcode #2: Add Two Numbers
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        
        # Build the two numbers as strings
        num1 = ""
        num2 = ""
        while l1:
            num1 = str(l1.val) + num1
            l1 = l1.next
        while l2:
            num2 = str(l2.val) + num2
            l2 = l2.next
        
        # Add them to find the solution
        num1 = int(num1)
        num2 = int(num2)
        num3 = num1 + num2
        num3 = str(num3)
        
        # Turn the solution into a reversed linked list.
        # Using a dummy node to construct the list
        dummy = ListNode(0)
        current = dummy
        # Going through the string backwards and creating linked nodes
        for i in reversed(num3):
            current.next = ListNode(int(i))
            current = current.next
        # The answer starts after our dummy
        return dummy.next

# Function to build linked lists for our test cases
def build_linked_list(array):
    dummy = ListNode(0)
    current = dummy
    for num in array:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# Function to turn linked lists back into arrays for printing
def list_to_array(list):
    current = list
    array = []
    while current:
        array.append(current.val)
        current = current.next
    return array


# Test case 1
l1 = build_linked_list([2,4,3])
l2 = build_linked_list([5,6,4])
result = addTwoNumbers(l1,l2)
print(list_to_array(result)) # [7,0,8]

# Test case 2
l1 = build_linked_list([0])
l2 = build_linked_list([0])
result = addTwoNumbers(l1,l2)
print(list_to_array(result)) # [0]

# Test case 3
l1 = build_linked_list([9,9,9,9,9,9,9])
l2 = build_linked_list([9,9,9,9])
result = addTwoNumbers(l1,l2)
print(list_to_array(result)) # [8,9,9,9,0,0,0,1]

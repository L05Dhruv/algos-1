# Sum List

# Write a function, sum_list, that takes in the head of a linked list containing numbers as an argument. 
# The function should return the total sum of all values in the linked list.

# Do not edit Class
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def sum_list(head):
  pass # todo


# TEST CASES
# 1. 
a = Node(2)
b = Node(8)
c = Node(3)
d = Node(-1)
e = Node(7)
a.next = b
b.next = c
c.next = d
d.next = e
sum_list(a) # -> 19

# 2.
# x = Node(38)
# y = Node(4)
# x.next = y
# sum_list(x) # -> 42

# 3.
# z = Node(100)

# 4.
# sum_list(z) # -> 100

# 5.
# sum_list(None) # -> 0

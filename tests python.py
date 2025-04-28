
# This function is in LinkedList class.
# Inserts a new node after the given prev_node. This method is
# defined inside LinkedList class shown above */

class Node: 
  
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data  # Assign data 
        self.next = None  # Initialize next as null 
  
# Linked List class 
  
  
class LinkedList: 
  
    # Function to initialize the Linked List object 
    def __init__(self): 
        self.head = None
        


def push(self, new_data):
 
    # 1 & 2: Allocate the Node &
    # Put in the data
    new_node = Node(new_data)
 
    # 3. Make next of new Node as head
    new_node.next = self.head
 
    # 4. Move the head to point to new Node
    self.head = new_node

def insertAfter(self, prev_node, new_data):
 
    # 1. check if the given prev_node exists
    if prev_node is None:
        print("The given previous node must inLinkedList.")
        return
 
    # 2. Create new node &
    # 3. Put in the data
    new_node = Node(new_data)
 
    # 4. Make next of new Node as next of prev_node
    new_node.next = prev_node.next
 
    # 5. make next of prev_node as new_node
    prev_node.next = new_node

def append(self, new_data):
 
        # 1. Create a new node
        # 2. Put in the data
        # 3. Set next as None
        new_node = Node(new_data)
 
        # 4. If the Linked List is empty, then make the
        # new node as head
        if self.head is None:
            self.head = new_node
            return
 
        # 5. Else traverse till the last node
        last = self.head
        while (last.next):
            last = last.next
 
        # 6. Change the next of last node
        last.next = new_node

def printList(self): 
        temp = self.head 
        while (temp): 
            print (temp.data, " -> ", end = '') 
            temp = temp.next
        print("")

l1=LinkedList()
l2=LinkedList()

append(l1,1)
append(l1,3)
append(l1,6)
append(l1,5)

append(l2,1)
append(l2,3)
append(l2,6)
append(l2,8)
from typing import List


class Solution:
    def maxMeetings(self, N : int, S : List[int], F : List[int]) -> List[int]:
        u = self.N
        return u

N = 6
S = {1,3,0,5,8,5}
F = {2,4,6,7,9,9} 
a=Solution(N,S,F)
N2 = 6
S2 = {0,1,0,5,7,8,2}
F2 = {3,4,1,7,9,9,3}
Solution.maxMeetings(N2,S2,F2)
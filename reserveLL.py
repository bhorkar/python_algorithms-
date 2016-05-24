# Python program to reverse a linked list 
# Time Complexity : O(n)
# Space Complexity : O(1)
 
 # Node class 
class Node:
      
         # Constructor to initialize the node object
             def __init__(self, data):
                         self.data = data
                         self.next = None


class LinkedList:
     
        # Function to initialize head
            def __init__(self):
                   self.head = None

            def push(self, new_data):
                   new_node = Node(new_data)
                   new_node.next = self.head
                   self.head = new_node

                    
            def printList(self):
                  temp = self.head
                  while(temp):
                         print temp.data
                         temp = temp.next
            def reserve(self):
                pre = None;
                curr = self.head;
                while( curr is not None):
                    next = curr.next;
                    curr.next = pre;
                    pre  = curr;
                    curr = next;
                self.head = pre;



                         # Driver program to test above functions
llist = LinkedList();
llist.push(20)
llist.push(4)
llist.printList()
llist.reserve()
llist.printList()
                           
                         

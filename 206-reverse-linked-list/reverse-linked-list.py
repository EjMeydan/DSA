# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #recursion solution 
        
        if not head or not head.next:          #base case if empty list or one node
            return head 

        new_head = self.reverseList(head.next) #reverse list from 2nd node if first part is = False
        head.next.next = head                  #head.next is now the tail of the reversed list so point back to original head 

        head.next = None                       #original head is new tail so .next of original should be = None

        return new_head                        #new reversed list start point / new head from reversed list


        #iteration

        #current_node = head 
        #previous_node = None

        #while current_node != None:
        #    next_node = current_node.next 
        #    current_node.next = previous_node
        #    previous_node = current_node
        #    current_node = next_node

        #return previous_node





        


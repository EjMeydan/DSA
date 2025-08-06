# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #Notes
        #current_node = head | set up the pointer as the beginning of the list
        #previous_node = none will help us build the reversed list. starting at none so the new end of our list will point to nothing
        #while loop that says while current_node != none keep iterating through nodes
        #start by creating temp pointer next_node = current_node.next to keep a reminder of node after current node
        #start reversal current_node.next = previous_node so our .next pointer now points to our previous_node (backwards)
        #previous_node = current_node moving the previous_node pointer to the position of the current_node
        #current_node = next_node moving the current_node pointer itself to the next node in the original list which saved at next_node
        #return previous_node when the loop is done as current_node will now be value none so our previous_node will be pointing at the new head of reversed list
        
        current_node = head 
        previous_node = None                                    
                                              
        while current_node != None:             
            next_node = current_node.next      
            current_node.next = previous_node   
            previous_node = current_node       
            current_node = next_node            
             
        return previous_node 




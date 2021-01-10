# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        curr_node = head
        while curr_node.next:
            print(curr_node.val, curr_node.next.val)
            if curr_node.val == curr_node.next.val:
                if (curr_node.next.next):
                    curr_node.next = curr_node.next.next
                else:
                    curr_node.next = None
                    break
            else:
                curr_node = curr_node.next
        return head


def buildLList(elems):
    if elems:
        head = ListNode(elems.pop(0))
    current_node = head
    while(elems):
        temp = ListNode(elems.pop(0))
        current_node.next = temp
        current_node = temp
    return head


def printList(head):
    while(head.next):
        print(head.val, end=" ")
        head = head.next
    print(head.val, end=" ")


if __name__ == '__main__':
    sol = Solution()
    elems = [1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4]
    head = buildLList(elems)
    head = sol.deleteDuplicates(head)
    printList(head)

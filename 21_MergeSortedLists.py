# Definition for singly-linked list.
import random


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def print_list(self, x):
        while x.next:
            print(x.val, end=" ")
            x = x.next
        print(x.val)

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (l1 == None):
            return l2
        if (l2 == None):
            return l1
        head = l1 if l1.val <= l2.val else l2
        while l1.next and l2.next:
            if (l1.val <= l2.val):
                while l1.next:
                    if (l1.next.val >= l2.val):
                        break
                    else:
                        print("Next l1")
                        l1 = l1.next
                temp = l2
                l2 = l2.next
                temp.next = l1.next
                l1.next = temp
                # l1 = l1.next
                print("Inserted l2 into l1")
                self.print_list(l1)
                print("Head")
                self.print_list(head)
            else:
                while l2.next:
                    if (l2.next.val >= l1.val):
                        break
                    else:
                        print("Next l2")
                        l2 = l2.next
                temp = l1
                l1 = l1.next
                temp.next = l2.next
                l2.next = temp
                # l2 = l2.next
                print("Inserted l1 into l2")
                self.print_list(l2)
        # print("--Done While--")
        # print("Head")
        # self.print_list(head)
        # print("l1")
        # self.print_list(l1)
        # print("l2")
        # self.print_list(l2)
        # Both lists have one element
        if (not (l1.next or l2.next)):
            if l1.val <= l2.val:
                l1.next = l2
            else:
                l2.next = l1
            return head
        # For single element in l1
        if (l1.next is None):
            if (l1.val <= l2.val):
                l1.next = l2
                l2 = l1
                return head
            while l2.next and l2.next.val <= l1.val:
                l2 = l2.next
            l1.next = l2.next
            l2.next = l1
            return head
        # For single element in l2
        if (l2.next is None):
            if (l2.val <= l1.val):
                l2.next = l1
                l1 = l2
                return head
            while l1.next and l1.next.val <= l2.val:
                l1 = l1.next
            l2.next = l1.next
            l1.next = l2
            return head
        return head


def build_list(n, var=None):
    if not n:
        return ListNode(None)
    if not var:
        var = sorted(random.sample(range(1, 20), n))
    head = ListNode(var[0], None)
    curr_node = head
    for i in range(1, n):
        curr_node.next = ListNode(var[i])
        curr_node = curr_node.next
    return head


if __name__ == '__main__':
    sol = Solution()
    l1 = build_list(2, [-9, 3])
    l2 = build_list(2, [5, 7])
    l1 = build_list(3, [1, 2, 4])
    l2 = build_list(3, [1, 3, 4])
    # l1 = build_list(8, [-10, -7, -6, -2, -1, -1, 0, 2])
    # l2 = build_list(3, [4, 6, 7])
    l1 = build_list(7, [-10, -10, -9, -4, 1, 6, 6])
    l2 = build_list(1, [-7])
    l2 = build_list(2, [10, 12])
    l1 = build_list(1, [11])
    l2 = build_list(3, [1, 3, 6])
    l1 = build_list(1, [-9])
    sol.print_list(l1)
    sol.print_list(l2)
    x = sol.mergeTwoLists(l1, l2)
    print("Result")
    sol.print_list(x)

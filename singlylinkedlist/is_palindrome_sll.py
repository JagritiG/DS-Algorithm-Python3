# Check if data stored in singly linked list is a palindrome
from singlylinkedlist.singly_linkedlist import Sll


def is_palindrome(head):

    # ToDo: Method 1: storing list data in a string
    # s = ""
    # current = head
    # while current:
    #     s += current.data
    #     current = current.next
    # return s == s[::-1]

    # ToDo: Method 2: using stack
    current = head
    s = []
    while current:
        s.append(current.data)
        current = current.next
    current = head
    while current:
        data = s.pop()
        if current.data != data:
            return False
        current = current.next
    return True

    # ToDo: Method 3: by traversing and comparing stored data from both ends
    # curr_1 = head
    # curr_2 = head
    # prev = []
    #
    # i = 0
    # while curr_2:
    #     prev.append(curr_2)
    #     curr_2 = curr_2.next
    #     i += 1
    # curr_2 = prev[i-1]
    #
    # count = 1
    # while count <= i//2 + 1:
    #     if prev[-count].data != curr_1.data:
    #         return False
    #     curr_1 = curr_1.next
    #     count += 1
    # return True


if __name__ == "__main__":

    sll = Sll()
    sll.add_at_tail("K")
    sll.add_at_tail("A")
    sll.add_at_tail("Y")
    sll.add_at_tail("A")
    sll.add_at_tail("K")
    print("List: ")
    sll.print_list()
    print("\n")
    print("Is Palindrome? " + str(is_palindrome(sll.head)))


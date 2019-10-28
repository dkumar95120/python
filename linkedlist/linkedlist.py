class SinglyLinkedListNode:
    def __init__(self, val=0):
        self.data = val
        self.next = None 

class SinglyLinkedList:
    def __init__(self,head=None):
        self.head = head 

    def insert_node(self, val):
        node = SinglyLinkedListNode(val)
        cur = tail = self.head
        while bool(cur):
            tail = cur
            cur = cur.next
        if bool(tail):
            tail.next = node
        else:
            self.head = node
        return

def findMergeNode(head1, head2):
    cur_node = head1
    while cur_node:
        other_node = head2
        while other_node and cur_node != other_node:
            other_node = other_node.next
        if cur_node == other_node:
            return cur_node.data
        cur_node = cur_node.next
    return -1
#     int data
#     SinglyLinkedListNode next
#
def insertNodeAtPosition(head, data, position):
    node = SinglyLinkedListNode(data)
    # Handle position = 0 as this would change the list head
    if position == 0:
        node.next = head
        return node

    i = 0
    cur = prev = head
    while cur and i < position:
        prev = cur
        cur = cur.next
        i += 1

    if bool(prev):
        prev.next = node
    node.next = cur

    return head

def deleteNodeAtPosition(head,position):
    if not bool(head):
        return None

    if position == 0:
        head = head.next
        return head

    cur = prev = head
    i = 0
    while i < position and bool(cur):
        prev = cur
        cur = cur.next
        i += 1

    prev.next = cur.next
    return head

def print_singly_linked_list(llist, delimiter):
    cur = llist.head
    while bool(cur):
        print (cur.data, end=delimiter)
        cur = cur.next
    print()

def has_cycle(head):
    single_freq = head
    double_freq = head.next
    while double_freq and single_freq != double_freq:
        single_freq = single_freq.next
        double_freq = double_freq.next
        if double_freq and double_freq != single_freq:
            double_freq = double_freq.next
    if double_freq:
        return 1
    else:
        return 0

if __name__ == '__main__':

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    data = int(input())

    position = int(input())

    llist_head = insertNodeAtPosition(llist.head, data, position)

    print_singly_linked_list(llist_head, ' ', fptr)

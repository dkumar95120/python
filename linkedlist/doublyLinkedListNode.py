class DoublyLinkedListNode:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

# Here is how the pointers for the nodes are going to be repaired
#
#     |<--prev--node--next-->|
#   prev--next---^^---prev--cur
#
#
def sortedInsert(head, data):
    node = DoublyLinkedListNode(data)
    cur = prev = head
    prev_val = 0
    while cur:
        if data >= prev_val and data < cur.data:
            if cur == head: # we have a new head of the list
                node.next = head
                head.prev = node
                head = node
                return head
            node.prev = prev
            node.next = cur
            cur.prev  = node
            prev.next = node
            break
        else:
            prev = cur
            prev_val = prev.data
            cur = cur.next
    # if this the largest value then append it to the list
    if not bool(cur):
        prev.next = node
        node.prev = prev
    return head
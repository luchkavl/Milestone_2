class Node:
    __slots__ = 'value', 'next_node'

    def __init__(self, value):
        self.value = value
        self.next_node = None


class LinkedList:

    def __init__(self, head):
        self.head = head

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next_node

    def __str__(self):
        return ' -> '.join(map(str, self))


head = Node(1)
head.next_node = Node(2)
head.next_node.next_node = Node(3)
head.next_node.next_node.next_node = Node(4)

linked_list = LinkedList(head)

print('Original:', linked_list)


def reverse(head):
    prev = None
    curr = head
    while curr:
        next = curr.next_node
        curr.next_node = prev
        prev = curr
        curr = next
    return prev

reversed_list = LinkedList(reverse(head))

print('Reversed:', reversed_list)

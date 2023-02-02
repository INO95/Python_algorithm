from typing import Any


class Node:
    def __init__(self, data: Any):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        temp = self.head

        while (temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()


Linked_list = LinkedList()

node1 = Node(11)
Linked_list.head = node1
node2 = Node(12)
node3 = Node(13)

node1.next = node2
node2.next = node3

Linked_list.traverse()

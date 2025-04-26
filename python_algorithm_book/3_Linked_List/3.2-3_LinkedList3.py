# 연결 리스트에서 맨 앞 요소 삽입

# 기존 head가 가지는 값을 변경하고 기존 head에 연결되었던 것은 새로운 노드의 next에 할당해 줘야함
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

    def push_back(self, data: any):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while (last.next):
            last = last.next

        last.next = new_node

    def push(self, data: Any):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        self.head = new_node
        new_node.next = temp


linked_list = LinkedList()

linked_list.push_back(11)
linked_list.push_back(12)
linked_list.push_back(13)

linked_list.push(10)

linked_list.traverse()

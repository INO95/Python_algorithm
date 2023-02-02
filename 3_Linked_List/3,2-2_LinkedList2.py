# 연결 리스트에서 맨 뒤 요소 삽입

# 수동으로 Node 객체를 생성하고 데이터를 초기화하여 next로 연결해 주는 과정을 구현
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


linked_list = LinkedList()

linked_list.push_back(11)
linked_list.push_back(12)
linked_list.push_back(13)

linked_list.traverse()

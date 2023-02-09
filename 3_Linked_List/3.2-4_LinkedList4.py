# 연결 리스트에서 특정 값을 가지는 노드 삭제하기

# 지워지는 노드의 이전 노드를 찾는다
# 찾은 이전 노드의 다음 노드를 변경한다
# 지워지는 노드를 메모리에서 삭제한다

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

    def remove(self, data: Any):
        curr = self.head
        prev = None

        # head의 요소가 지워지는 요소일 때 처리
        if curr is not None:
            if curr.data == data:
                self.head = curr.next
                curr = None
                return

        while (curr is not None):
            if curr.data == data:
                break
            prev = curr
            curr = curr.next

        # 지우려는 data 노드를 찾지 못했을 때 처리
        if curr == None:
            return

        prev.next = curr.next

        curr = None

    def remove_node(self, node: Node):
        if node == None:
            return

        if node.next == None:
            node = None
            return

        next_node = node.next
        node.val = next_node.val
        node.next = next_node.next

        next_node = None


linked_list = LinkedList()

linked_list.push_back(11)
linked_list.push_back(12)
linked_list.push_back(13)

linked_list.push(10)

linked_list.remove(13)

linked_list.remove_node(11)

linked_list.traverse()
# 날먹ㅋ5

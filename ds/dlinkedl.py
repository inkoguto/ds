import random


class Node:
    data = None
    next = None
    prev = None

    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.data)


class Dlinkedl:
    head = None
    last = None
    length = 0

    def insert_at_begin(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.last = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
        self.length += 1

    def insert_at_end(self, data):
        node = Node(data)
        self.last.next = node
        node.prev = self.last
        self.last = node
        self.length += 1

    def delete(self, node):
        pass

    def delete_first(self):
        head = self.head
        self.head = head.next
        self.head.prev = None
        head = None
        self.length -= 1

    def delete_last(self):
        last = self.last
        self.last = last.prev
        self.last.next = None
        last = None

        self.length -= 1

    def insert(self, node, data):
        new_node = Node(data)
        next = node.next
        node.next = new_node
        new_node.prev = node
        next.prev = new_node
        new_node.next = next

    def find(self, data):
        current = self.head
        while (current is not None):
            if current.data == data:
                return current
            current = current.next

        return None

    def display_forward(self):
        str_rpr = ""
        current = self.head
        while current is not None:
            str_rpr = self._format(str_rpr, current, current.next)
            current = current.next

        print(str_rpr)

    def display_backward(self):
        str_rpr = ""
        current = self.last
        while (current is not None):
            str_rpr = self._format(str_rpr, current, current.prev)
            current = current.prev
        print(str_rpr)

    @staticmethod
    def _format(string, data, last):
        if last is not None:
            string += "{},".format(data)
        else:
            string += "{}".format(data)

        return string

    def sort(self):
        for _ in range(0, self.length):
            current = self.head
            while current.next is not None:
                if current.data > current.next.data:
                    tmp = current.data
                    current.data = current.next.data
                    current.next.data = tmp
                current = current.next

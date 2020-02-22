class Node:
    value = None
    next = None

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class LinkedList:
    head = None

    def traverse(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next

    def insert_at_begin(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, value):
        *_, last = self.traverse()
        last.next = Node(value)

    def insert(self, node, value):
        new_node = Node(value)
        new_node.next = node.next
        node.next = new_node

    def delete(self, key):
        if self.head.value == key:
            self.head = self.head.next
            return

        for node in self.traverse():
            if node.next.value == key:
                node.next = node.next.next
                break

    def reverse(self):
        current = self.head
        prev = None
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next

        self.head = prev

    def search(self, key):
        for node in self.traverse():
            if node.value == key:
                return node

        return None

    def __str__(self):
        representation = "["
        for node in self.traverse():
            if node.next is not None:
                representation += "{}, ".format(node.value)
            else:
                representation += "{}".format(node.value)

        return "{}]".format(representation)

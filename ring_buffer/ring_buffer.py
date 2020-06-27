from dll import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = DoublyLinkedList()
        self.current = None

    def append(self, item):
        if self.storage.length == 0:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail

        elif self.storage.length == self.capacity:
            if self.current == self.storage.tail:
                self.current = self.storage.head
            else:
                self.current = self.current.next

            self.current.value = item

        else:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail

    def get(self):
        node_list = []
        current_node = self.storage.head

        while current_node is not None:
            if current_node.value is not None:
                node_list.append(current_node.value)
                current_node = current_node.next

        return node_list

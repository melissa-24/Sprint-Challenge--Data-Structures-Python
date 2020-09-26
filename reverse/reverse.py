class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # Thoughts for layout to cover everything if list is empty I am thinking have it return None and same if there is 1 item.  as these can not be reversed but maybe that is too much. So just if its empty otherwise just reverse. You just wont notice a change if there is 1 items.  Otherwise too  many lines of code
        if self.head is None:
            return None
            # thats the easy part
        if node.next_node is None:
            self.head = node
            return
        self.reverse_list(node.next_node, None)
        following = node.next_node
        following.next_node = node
        node.next_node = None

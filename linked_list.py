from typing import Optional, Iterable, Any
from node import Node


class LinkedList:
    def __init__(self, data: Iterable = None):
        self.len = 0
        self.begin: Optional["Node"] = None
        self.list_nodes = []
        # if data is not None:
        #     self.init_list_nodes(data)
        if data is not None:
            for el in data:
                self.append(el)

    # def init_list_nodes(self, data: Iterable = None):
    #     for el in data:
    #         self.list_nodes.append(Node(el))
    #     self.begin = self.list_nodes[0]
    #     self.len = len(self.list_nodes)
    #     for i in range(len(self.list_nodes) - 1):
    #         current_node = self.list_nodes[i]
    #         next_node = self.list_nodes[i + 1]
    #         self.linked_nodes(current_node, next_node)

    @staticmethod
    def linked_nodes(current_node: Node, next_node: Optional["Node"] = None):
        current_node.next = next_node

    def step_by_step_on_nodes(self, index: int):
        if not isinstance(index, int):
            raise TypeError
        if not 0 <= index < self.len:
            raise IndexError
        current_node = self.begin
        for _ in range(index): ## index = 4  [0..3] [0..4)
            current_node = current_node.next
        return current_node #return Node.value = 5

    def append(self, value: Any):
        node = Node(value)
        if self.begin is None:
            self.begin = node
        else:
            last_node = self.step_by_step_on_nodes(self.len - 1)
            self.linked_nodes(last_node, node)
        self.len += 1

    def index(self, value):
        ind = 0
        for node in self:
            if node == value:
                return ind
            ind += 1
        raise ValueError('Value is not found')

    def insert(self, index: int, value: Any):
        if not isinstance(index, int):
            raise TypeError
        if not 0 <= index <= self.len:
            raise IndexError
        if index == 0:
            self.begin = Node(value, self.begin)
            self.len += 1
        elif 0 < index < self.len:
            left_node = self.step_by_step_on_nodes(index - 1)
            left_node.next = Node(value, left_node.next)
            self.len += 1
        else:
            self.append(value)

    def extend(self, data: Iterable):
        for el in data:
            self.append(el)

    def pop(self, index: int = -1):
        if not isinstance(index, int):
            raise TypeError
        if abs(index) >= self.len:
            raise IndexError('Pop index out of range')
        if index >= 0:
            current_node = self[index]
            del self[index]
        else:
            current_node = self[self.len + index]
            del self[self.len + index]
        return current_node


    def __getitem__(self, index: int):
        node = self.step_by_step_on_nodes(index)
        return node.value

    def __str__(self):
        return f'{[node for node in self]}'

    def __len__(self):
        return self.len

    def __delitem__(self, index: int):
        if not isinstance(index, int):
            raise TypeError
        if not 0 <= index <= self.len:
            raise IndexError
        if index == 0:
            self.begin = self.begin.next
        elif index == self.len - 1:
            prev_node = self.step_by_step_on_nodes(index - 1)
            prev_node.next = None
        else:
            left_node = self.step_by_step_on_nodes(index - 1)
            del_node = left_node.next
            self.linked_nodes(left_node, del_node.next)
        self.len -= 1



if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    linked_list = LinkedList(data)
    print()
    for el in linked_list:
        print(el)
    print(len(linked_list))
    linked_list.append(6)
    print(linked_list)
    print(linked_list.index(4))
    print('###############')
    linked_list.insert(0, 10)
    print(linked_list)
    linked_list.extend((11, 21, 13))
    print(linked_list)
    print(linked_list.pop(-5))
    print(linked_list)

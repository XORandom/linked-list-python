from typing import Any, Optional

class Node:
    def __init__(self, value: Any, next_: Optional["Node"]=None):
        self.__value = value
        self.next = next_

    @property
    def value(self):
        return self.__value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next_: Optional["Node"] = None):
        self.is_valid(next_)
        self.__next = next_

    def is_valid(self, node):
        if not isinstance(node, (Node, type(None))):
            raise TypeError

    def __str__(self):
        return str(self.__value) #f'{self.value}'

    def __repr__(self):
        if self.__next is None:
            return f'{self.__class__.__name__}({self.__value}, {None})'
        else:
            return f'{self.__class__.__name__}({self.__value}, Node({self.__next}))'


if __name__ == '__main__':
    first_node = Node(1)
    second_node = Node(2)
    print(first_node, second_node)
    list_nodes = [first_node, second_node]
    print(list_nodes)
    first_node.next = second_node
    print(first_node.next)
    print(list_nodes)

#!/usr/bin/python3
"""The module for linked lists
"""


class Node:
    """THis is the node logic
    """
    def __init__(self, data, next_node=None):
        """Initializes data and next node through the properties

        Args:
            data (int): integer for the node
            next_node (Node): the next node to be added. Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """getter for data

        Returns:
            int: the integer for the node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """data setter

        Args:
            value (int): The integer for the node

        Raises:
            TypeError: In case the data is not the expected
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """The node

        Returns:
            Node: the next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """THe next node setter

        Args:
            value (Node): The next node

        Raises:
            TypeError: In case the value is not the expected one
        """
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

    def __str__(self):
        """The node as a string

        Returns:
            str: Node as a string
        """
        return str(self.__data)


class SinglyLinkedList:
    """The whole logic for the singly linked list
    """
    def __init__(self):
        """Initializes head
        """
        self.__head = None

    def sorted_insert(self, value):
        """Inserts in a sorted manner

        Args:
            value (node): The new node
        """
        node = Node(value)
        fut = self.__head
        if fut is None or node.data < fut.data:
            if fut is None:
                self.__head = node
                return
            else:
                node.next_node = self.__head
                self.__head = node
                return
        while fut.next_node is not None and fut.next_node.data < node.data:
            fut = fut.next_node
        node.next_node = fut.next_node
        fut.next_node = node

    def __str__(self):
        """Prints the info

        Returns:
            string: a string
        """
        pri = ""
        act = self.__head
        while act is not None:
            if act.next_node is not None:
                pri += str(act) + "\n"
            else:
                pri += str(act)
            act = act.next_node
        return pri

#!/usr/bin/python3
"""This module contains a rebel Int class :D
Long live the rebelion >.<
"""


class MyInt(int):
    """Rebel class reporting for the republic rebelion

    Args:
        int (class): SUper class imperial
    """
    def __eq__(self, other):
        """Inverts equaliy

        Args:
            other (object): Other object

        Returns:
            bool: True or False
        """
        return int(self) != int(other)

    def __nq__(self, other):
        """Inverts inequality

        Args:
            other (object): Other object

        Returns:
            bool: True or False
        """
        return int(self) == int(other)

# data-structures

This repository contains sample code for a number of classic data structures
implemented in Python.

Use the Doubly Linked List or cases where a user may need to reference a 
previous item in the list from any given item, or where a user may need to 
iterate through the list in reverse order. Otherwise, use the slightly faster
Singly Linked List.

proper_parens:
    This function takes a unicode string (text) as input and returns one of three possible values:
      - Return 1 if the string is “open” (there are open parens that are not closed)
      - Return 0 if the string is “balanced” (there are an equal number of open and closed parentheses in the string)
      - Return -1 if the string is “broken” (a closing parens has not been proceeded by one that opens)

Singly Linked List:
    Module linked_list.py contains a recursively generated linked list class
    (Linked_List).

Stack:
    Module stack.py leverages the linked_list module to build methods for
    generating a stack, as well as adding and removing items.

Doubly Linked List:
    Module dbl_linked_list.py contains a DblLinkedList class with pop, shift,
    insert, append and remove methods. It also contains a Node class, which
    DblLinkedList uses to hold its values.


Resources:

    https://www.codefellows.org/blog/implementing-a-singly-linked-list-in-python

    http://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementinganUnorderedListLinkedLists.html

    http://stackoverflow.com/questions/31333462/finding-the-length-of-a-linked-list-in-python

    https://en.wikipedia.org/wiki/Linked_list

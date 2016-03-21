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

Queue:
    Module new_queue.py contains a Queue class with enqueue, dequeue, and size
    methods, as well as a peek method that allows the user to get the value of
    the next item in the queue without popping it. The Queue class imports the
    DblLinkedList class described above, and most of its methods are composed
    from this class.

Deque:
    Module new_deque.py contains a Deque class with methods for appending to
    both ends of the deque, removing items from each end of the deque, "peeking"
    at the values of the items on each end, and calculating the size of the
    deque. The Deque class imports the DblLinkedList class, and most of its
    methods are composed from this class.


Resources:

    https://www.codefellows.org/blog/implementing-a-singly-linked-list-in-python

    http://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementinganUnorderedListLinkedLists.html

    http://stackoverflow.com/questions/31333462/finding-the-length-of-a-linked-list-in-python

    https://en.wikipedia.org/wiki/Linked_list

# This exercise is a cautionary tale about one of the most common, and difficult to find, errors in Python.
# Write a definition for a class named Kangaroo with the following methods:
#
#     An __init__ method that initializes an attribute named pouch_contents to an empty list.
#     A method named put_in_pouch that takes an object of any type and adds it to pouch_contents.
#     A __str__ method that returns a string representation of the Kangaroo object and the contents of the pouch.
#
# Test your code by creating two Kangaroo objects, assigning them to variables named kanga and roo, and then adding roo to the contents of kanga’s pouch.
#
# Download http://thinkpython2.com/code/BadKangaroo.py. It contains a solution to the previous problem with one big, nasty bug. Find and fix the bug.
#
# If you get stuck, you can download http://thinkpython2.com/code/GoodKangaroo.py, which explains the problem and demonstrates a solution.

class Kangaroo:
    def __init__(self):
        self.pouch_contents = []

    def put_in_pouch(self, object_to_add):
        self.pouch_contents.append(object_to_add)
        return

    def __str__(self):
        return f"Contents of pouch:{self.pouch_contents}"

    def __repr__(self):
        return f"Kangaroo with pouch contents:{self.pouch_contents}"

kanga = Kangaroo()
roo = Kangaroo()

kanga.put_in_pouch(roo)

print(kanga)

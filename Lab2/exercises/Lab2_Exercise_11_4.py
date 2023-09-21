# Exercise 11.4. If you did Exercise 10.7, you already have a function named has_duplicates that
# takes a list as a parameter and returns True if there is any object that appears more than once in the
# list

# Use a dictionary to write a faster, simpler version of has_duplicates. Solution: http: //
# thinkpython2. com/ code/ has_ duplicates. py

# Do the lists contain objects or strings?

test_list_duplicates = ["fish", 5, 3.4, "fish"]
test_list_non_duplicates = ["fish", 5, 3.4]


def has_duplicates(list_to_check):
    item_dict = {}
    for item in list_to_check:
        if isinstance(item, str):
            text_repr = item
        else:
            text_repr = str(item)
        if text_repr in item_dict:
            if item_dict[text_repr] == item:
                return True
        else:
            item_dict[text_repr] = item
    return False


print(has_duplicates(test_list_duplicates))
print(has_duplicates(test_list_non_duplicates))

# Exercise 10.11. Two words are a “reverse pair” if each is the reverse of the other. Write a program
# that finds all the reverse pairs in the word list. Solution: http: // thinkpython2. com/ code/
# reverse_ pair. py

word_list = ["rail", "fish", "liar", "deliver", "reviled", "apple", "rat", "banana", "tar", "denim", "mined", "rats",
             "star"]


def reverse_string(input_string):
    input_array = list(input_string)
    input_array.reverse()
    output = ""
    for i in input_array:
        output += i
    return output


def print_solution(solution_array):
    print("The reverse pairs are:")
    for pair in solution_array:
        print(pair[0], pair[1])


def find_pairs(word_list):
    found_list = []
    found_pairs = []
    for i, word in enumerate(word_list):
        reversed_word = reverse_string(word)
        if reversed_word in word_list and not word in found_list:
            found_list.append(word)
            found_list.append(reversed_word)
            found_pairs.append([word, reversed_word])
    return found_pairs


print_solution(find_pairs(word_list))

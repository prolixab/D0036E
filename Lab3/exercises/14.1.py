# Exercise 1
# Write a function called sed that takes as arguments a pattern string, a replacement string, and two filenames;
# it should read the first file and write the contents into the second file (creating it if necessary).
# If the pattern string appears anywhere in the file, it should be replaced with the replacement string.
# If an error occurs while opening, reading, writing or closing files, your program should catch the exception, print an error message, and exit.
# Solution: http://thinkpython2.com/code/sed.py.


def sed(pattern, replacement, filename_1, filename_2):
    try:
        with open(filename_1, "r") as f:
            with open(filename_2, "w") as g:
                for line in f:
                    replaced_line = line.replace(pattern, replacement)
                    g.writelines(replaced_line)
    except Exception as e:
        print(f"An error was encountered: {e}")


sed("as", "en", "file1.txt", "file2.txt")

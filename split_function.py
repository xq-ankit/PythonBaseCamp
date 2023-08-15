str="john is good student"
print(str.split (' ',2))


# the split() function is a built-in method in Python that allows you to split a string into a list of substrings 
# based on a specified separator.By default, the separator used by the split() function is the whitespace character, 
# which includes spaces, tabs, and newlines.

# The basic syntax of the split() function is as follows:
# string.split(separator, maxsplit)
# Here, string is the string you want to split, separator is the character 
# or substring to use as the separator, and maxsplit is an optional parameter that specifies the maximum number of splits to make.

# When you call the split() function on a string, it returns a list of the substrings
# that were separated by the specified separator. For example, consider the following code:

# sentence = "The quick brown fox jumped over the lazy dog."
# words = sentence.split()
# print(words)
# The split() function is called on the string sentence, which contains a sentence with multiple words. 
# Since no separator is specified, the function uses the default whitespace separator and splits the sentence into a list of words. 
# The resulting list is then stored in the variable words, which is printed to the console. The output of this code would be:


# ['The', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog.']
# In addition to the default whitespace separator, you can also specify a custom separator to use with the split() function. 
# For example, consider the following code:

# numbers = "1,2,3,4,5"
# list_of_numbers = numbers.split(",")
# print(list_of_numbers)
# In this case, the string numbers contains a series of numbers separated by commas. The split() function is called with a comma separator specified as an argument. 
# The resulting list of numbers is then printed to the console. The output of this code would be:


# ['1', '2', '3', '4', '5']
# As you can see, the split() function is a useful method for splitting a string into smaller substrings based on a specified separator.


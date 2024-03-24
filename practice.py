""" # Create a dictionary with one key-value pair
my_dict = {"name": "John"}

# Print the result of comparing two views of the dictionary values
# Note: my_dict.values() creates a new view object each time it's called hence return False
print(my_dict.values() == my_dict.values()) """


""" print(help("keywords")) """


""" #In Python, the comparison operators, such as > (greater than), work based on the Unicode code points of the characters in the strings. 
#In Unicode, lowercase letters have higher code points than their corresponding uppercase letters.
print("hello" > "Hello" > "HELLO") """

def word_even(s):
    even_char = s[0::2]
    print(even_char)

word = input('Enter word : ')
print("Original String:", word)

word_even(word)

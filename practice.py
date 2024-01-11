# Create a dictionary with one key-value pair
my_dict = {"name": "John"}

# Print the result of comparing two views of the dictionary values
# Note: my_dict.values() creates a new view object each time it's called hence return False
print(my_dict.values() == my_dict.values())

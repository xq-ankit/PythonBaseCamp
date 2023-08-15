# Creating a dictionary
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# len(dict)
print(len(my_dict))  # Output: 3

# dict.keys()
print(my_dict.keys())  # Output: dict_keys(['name', 'age', 'city'])

# dict.values()
print(my_dict.values())  # Output: dict_values(['John', 30, 'New York'])

# dict.items()
print(my_dict.items())  # Output: dict_items([('name', 'John'), ('age', 30), ('city', 'New York')])

# dict.get(key[, default])
print(my_dict.get('name'))  # Output: John
print(my_dict.get('gender', 'Unknown'))  # Output: Unknown

# dict.pop(key[, default])
age = my_dict.pop('age')
print(age)  # Output: 30
print(my_dict)  # Output: {'name': 'John', 'city': 'New York'}

# dict.popitem()
item = my_dict.popitem()
print(item)  # Output: ('city', 'New York')
print(my_dict)  # Output: {'name': 'John'}

# dict.clear()
my_dict.clear()
print(my_dict)  # Output: {}

# dict.copy()
new_dict = {'name': 'Jane', 'age': 25}
copied_dict = new_dict.copy()
print(copied_dict)  # Output: {'name': 'Jane', 'age': 25}

# dict.update(other_dict)
other_dict = {'city': 'London', 'country': 'UK'}
new_dict.update(other_dict)
print(new_dict)  # Output: {'name': 'Jane', 'age': 25, 'city': 'London', 'country': 'UK'}

# dict.setdefault(key[, default])
name = new_dict.setdefault('name', 'Unknown')
print(name)  # Output: Jane
gender = new_dict.setdefault('gender', 'Unknown')
print(gender)  # Output: Unknown
print(new_dict)  # Output: {'name': 'Jane', 'age': 25, 'city': 'London', 'country': 'UK', 'gender': 'Unknown'}

# dict.fromkeys(seq[, value])
keys = ['name', 'age', 'city']
default_value = 'Unknown'
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)  # Output: {'name': 'Unknown', 'age': 'Unknown', 'city': 'Unknown'}

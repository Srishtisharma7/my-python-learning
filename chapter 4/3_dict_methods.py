# Initialize a dictionary
person = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York',
    'profession': 'Engineer'
}

# Accessing keys, values, and items
print("Keys:", person.keys())            # dict_keys(['name', 'age', 'city', 'profession'])
print("Values:", person.values())        # dict_values(['Alice', 25, 'New York', 'Engineer'])
print("Items:", person.items())          # dict_items([('name', 'Alice'), ('age', 25), ('city', 'New York'), ('profession', 'Engineer')])

# Retrieving a value
print("Name:", person.get('name'))       # Alice
print("Country:", person.get('country', 'Not specified'))  # Not specified

# Adding or updating values
person['age'] = 26                       # Update existing key
person['country'] = 'USA'                # Add a new key-value pair
print("Updated dictionary:", person)

# Using update to add multiple values
person.update({'hobby': 'Painting', 'city': 'Boston'})
print("After update:", person)

# Using setdefault
default_value = person.setdefault('language', 'English')  # Adds 'language' if not present
print("Set default value for 'language':", default_value)
print("Dictionary after setdefault:", person)

# Removing items
age = person.pop('age')                  # Remove 'age' key and return its value
print("Popped age:", age)
print("Dictionary after pop:", person)

last_item = person.popitem()             # Remove the last key-value pair
print("Popped last item:", last_item)
print("Dictionary after popitem:", person)

# Using clear to remove all items
person.clear()
print("Dictionary after clear:", person)

# Copying a dictionary
new_person = {'name': 'Bob', 'age': 30}
copied_person = new_person.copy()        # Creates a shallow copy
print("Copied dictionary:", copied_person)

# Using fromkeys to create a new dictionary
keys = ['x', 'y', 'z']
default_dict = dict.fromkeys(keys, 0)
print("New dictionary from keys:", default_dict)


#output:
# Keys: dict_keys(['name', 'age', 'city', 'profession'])
# Values: dict_values(['Alice', 25, 'New York', 'Engineer'])
# Items: dict_items([('name', 'Alice'), ('age', 25), ('city', 'New York'), ('profession', 'Engineer')])
# Name: Alice
# Country: Not specified
# Updated dictionary: {'name': 'Alice', 'age': 26, 'city': 'New York', 'profession': 'Engineer', 'country': 'USA'}
# After update: {'name': 'Alice', 'age': 26, 'city': 'Boston', 'profession': 'Engineer', 'country': 'USA', 'hobby': 'Painting'}
# Set default value for 'language': English
# Dictionary after setdefault: {'name': 'Alice', 'age': 26, 'city': 'Boston', 'profession': 'Engineer', 'country': 'USA', 'hobby': 'Painting', 'language': 'English'}
# Popped age: 26
# Dictionary after pop: {'name': 'Alice', 'city': 'Boston', 'profession': 'Engineer', 'country': 'USA', 'hobby': 'Painting', 'language': 'English'}
# Popped last item: ('language', 'English')
# Dictionary after popitem: {'name': 'Alice', 'city': 'Boston', 'profession': 'Engineer', 'country': 'USA', 'hobby': 'Painting'}
# Dictionary after clear: {}
# Copied dictionary: {'name': 'Bob', 'age': 30}
# New dictionary from keys: {'x': 0, 'y': 0, 'z': 0}

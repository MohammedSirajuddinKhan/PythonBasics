# A dictionary is a collection of key-value pairs. Each key is unique and maps to a value.

d={"name": "Alice", "age": 30, "city": "New York"}
print(d)

# Accessing values using keys
print(d["name"])  # Output: Alice
print(d.get("age"))  # Output: 30
print(d.get("city"))  # Output: New York

# Adding or updating key-value pairs
d["age"] = 31  # Update age
d["country"] = "USA"  # Add new key-value pair
print(d)

# Removing key-value pairs
del d["city"]  # Remove key "city"
print(d)

# Looping through a dictionary
for key, value in d.items():
    print(key, ":", value)

# Checking if a key exists in the dictionary
if "name" in d:
    print("Name exists in the dictionary.")
print(d.keys())  # Output: dict_keys(['name', 'age', 'country'])
# Given a list of names, find and print the name that appears the most in the list.


names = ["Alice", "Bob", "Alice", "Charlie", "Bob", "Alice", "David", "Charlie"]


name_count = {}


for name in names:
    if name in name_count:
        name_count[name] += 1
    else:
        name_count[name] = 1


most_common_name = max(name_count, key=name_count.get)
most_common_count = name_count[most_common_name]

print(names)
print(f"The name that appears the most is '{most_common_name}' with {most_common_count} occurrences.")

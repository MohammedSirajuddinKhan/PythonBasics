# Tuples are Immutable sequences so we cannot change it once it is created

a = (1, 2, 3, 4, 5)
print(a)
print(len(a))

# Values can be accessed using index
print(a[-1])
print(a[0])

# No changes after tuple creation
# a[0]=10
# print(a)

# Methods
print(a.index(3)) # Returns the index of the first occurrence of 3
print(a.count(2)) # Returns the number of occurrences of 2
# # Lists are ordered so i can access anything at anytime
# a = [1, 2, 3, 4, 5]
# print(a[-1])
# print(a[2])

# # Lists are mutable so i can change anything at anytime unlike strings
# a[0] = 10
# print(a)

# Lists can store duplicates
# b = [1,1,1,1,2,2,2,3,3,3,4,4,4]
# print(b)

# Traversing on a list
a = [10,20,30,40,50]

## traversing on values
for i in a:
    print(i)

## traversing on index
for i in range(len(a)):
    print(a[i])

# Lists are heterogenous - they can store different types of data
a.append(60)
a.append("Sirajuddin")
a.append([1,2,3,4,5])
a.append({"Age":21})
print(a)

# Values can be inserted into Lists at any index
a.insert(0,"Start")
print(a)

# Values can be removed from Lists
a.remove("Start")
print(a)

# Last items can be removed from Lists
a.pop()
print(a)

# Lists can be sorted
# a.sort() # This wont work because the list is heterogenous and contains different types of data
# print(a)

# Lists can be reversed
a.reverse()
print(a)

# Length of a list can be found using len()
len(a)
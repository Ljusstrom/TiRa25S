a = 5
print(a)
b = a
print(b)

a = 7
print(a)
print(b)

c = [ 1, 2, 3]
d = c[:] # copy
print(c)
d[0] = 100
print(c)
print(d)


list_var = ['a', 'b', 'c', 10, 20, True] # It can contain different types
tuple_var = ('a', 'b', 'c', 10, 20, True) # It can contain different types, but tuple can't be modified after creation
set_var = {'a', 'b', 'c', 10, 20, True} # It can contain different types but not duplicates
string_var = "abc" # It can contain only characters
# Indexing:
print(list_var[0]) # 'a'
print(tuple_var[0]) # 'a'
print(string_var[0]) # 'a'
# Set's elements can't be accessed with indexing
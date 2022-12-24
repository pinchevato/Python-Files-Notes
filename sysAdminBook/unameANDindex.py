#demonstrates usage of index() (index() is about the same) for starting indexing characters in a string
foo="Neil is cool"
a=foo.index('cool')
print(foo)
print("\nStarting at line number %s" % a)
print(foo[a:])
print("\nAnd everything before line %s" % a)
print(foo[:a])
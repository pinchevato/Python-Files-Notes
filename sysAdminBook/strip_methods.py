spacious_string = "\n\t Some Non-Spacious Text\n \t\r"
print("a silly string w carriage return n tab before")
print(spacious_string)

print("remove spaces, tabs, carriage returns from beginning")
print(spacious_string.lstrip())
print(stripped)
print("remove spaces, tabs, carriage returns from end")
print(spacious_string.rstrip())
print(stripped)
print("remove ALL spaces, tabs, carriage returns")
stripped = spacious_string.strip()
print(stripped)

print("also remove specific characters from beg or end")
print(stripped.lstrip("Some "))
print(stripped.rstrip(" Text"))
print("remove characters from beg AND end")
print(stripped.strip("Some ").strip(" Text"))
#doesn't search for exact string to exactly match
#"Some  Text" and remove any occurrences of those
#two characters that are adjacent to one another
#in that order; it means remove any occurrences
#of "Some " or " Text" that are adjacent to one
#another on either end of the string
print("...a quicker way to do the same thing")
print(stripped.strip("Some  Text"))

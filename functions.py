def rev(text):
    return text[::-1]

print(rev("Don't worry, be happy!"))

print(rev([4, 3, 2, 1]))

def string_join(*strings):
    joined_string = ""
    for string in strings:
        joined_string = joined_string + " " + string
    return joined_string

print(string_join("Add", "multiple", "arguments"))
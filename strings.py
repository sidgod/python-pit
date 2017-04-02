name = "sidgod"

print(type(name))

# Notice single quote to encapsulate double quote
message = 'Say "Hellow World"'
print(message)

paragraph = """
First line
Second line
Third line
"""
print(paragraph)

hello = "Hello World!"
print(hello)

log_line = 'something broke src ip "10.211.230.171" dst ip "10.211.230.178"'
print(log_line.count('"'))
print(log_line.count("ip"))
print(log_line.replace('"', '\\\"'))
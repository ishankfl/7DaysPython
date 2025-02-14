#  Handling Division by Zero (ZeroDivisionError)

# Handling File Not Found (FileNotFoundError)

# Handling Invalid Type (TypeError)

# Handling Invalid Index (IndexError)
# try:
#     print(5*)
# except SyntaxError as e:
#     print("Syntax error")

file = open("example.txt", "r+")  # Open file in write mode
file.write("This is new content.\n")
file.write("The old content is erased.\n")
file.seek(4)
hi =file.read()

print(hi)
hello = hi.strip()
print(hello)

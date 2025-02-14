file = open("example.txt", "r")  # Open file in read mode
content = file.read()  # Read the file
print(content)  # Print the full content at once
file.close()  # Close the file

print("----------AfterStrip-------------")
file = open("example.txt", "r")  # Open file again in read mode
for line in file:
    print(line.strip())  # Print each line after removing leading/trailing spaces and newlines
file.close()

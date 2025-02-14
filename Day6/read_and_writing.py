
# Does not erase content, allows both reading and writing.
#to open file and different mode:
# syntax:
    # open(<---filename-->,<---mode-->)

file = open("example.txt", "r+")  # Read & Write mode
content = file.read()  # Read existing content
file.write("\nNew content added.")  # Add new content
file.close()

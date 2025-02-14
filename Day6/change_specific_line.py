
# Modify a specific line without affecting others.

file = open("example.txt", "r")
lines = file.readlines()  # Read all lines
file.close()

lines[1] = "This is the new second line.\n"  # Modify line 2

file = open("example.txt", "w")
file.writelines(lines)  # Write updated content
file.close()

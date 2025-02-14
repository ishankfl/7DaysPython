# Read the file, modify the text, and write it back.


file = open("example.txt", "r")
content = file.read()
file.close()

new_content = content.replace("old_word", "new_word")

file = open("example.txt", "w")
file.write(new_content)
file.close()

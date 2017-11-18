# Files that were going to open
filename = 'words.txt'
file_two = 'new_words.txt'

# Variables were going to use in program

# Program Lists to transfer long words
words = []
# long_words = []

# We open the file and store it into our list here
with open(filename, 'r') as file_object:
    for line in file_object:
        words.append(line.rstrip("\n"))

# We transfer the info into the new file
with open(file_two, 'w') as file:
    for x in words:
        if len(x) >= 5:
            file.write(x + '\n')

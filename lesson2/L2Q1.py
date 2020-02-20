file = open("show_version.txt")
#create a single string variable with all text from file
show_ver = file.read()

print(show_ver)
print(type(show_ver))

file.close()

#create a list called show_ver, where all lines in file are items in list
with open("show_version.txt") as file:
    show_ver = file.readlines()

print("\n")
print(show_ver)
print(type(show_ver))

#print each line in show_ver individually
for line in show_ver:
    print(line)
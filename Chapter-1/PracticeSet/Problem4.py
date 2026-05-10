import os

# Give path of the directory whose content you want to list
path = "." # Here "." represents the current directory.
# / for c: drive 

# Print all files and folders in the directory
contents = os.listdir(path) # Gives all file/folder names from that directory, Stored as → Python list

print("Contents of the directory:")
print(contents)

# for item in contents:
#     print(item)
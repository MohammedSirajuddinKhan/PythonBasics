# File Writing Basics

file = open("FileHandling.txt","w") # This will create a new file or overwrite an existing file

data = input("Likhna kya hai..?: ")

file.write(data)

file.close()

# File Updating Basics (Append)

with open("fileHandling.txt","a") as file:
    data = input("Ab kya likhna hai..?: ")
    file.write(data)
    
# File Reading Basics

file = open("fileHandling.txt","r") # This will open the file in read mode

content = file.read()

print(content)

file.close()


path = input()


extension = path.split(".")
extension_name = extension[-1]

name = path.split("\\")
name1 = name[-1].split(".")
file_name = name1[0]
print(f"File name: {file_name}")
print(f"File extension: {extension_name}")


#File Read and Write
with open("test.txt", "w") as f:
 f.write("Hello All!")
with open("test.txt", "r") as f:
 content = f.read()
 print("File content:", content)
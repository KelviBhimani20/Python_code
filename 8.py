# Iterative Statements
with open("test.txt", "w") as f:
 f.write("Hello Students!")
with open("test.txt", "r") as f:
 content = f.read()
 print("File content:", content)
 
 with open("source.txt", "r") as src, open("copy.txt", "w") as dst:
    dst.write(src.read())
    
#Python programs to print patterns
for i in range(1, 8):
 print(str(i) * i)
 
 for i in range(1, 8):
  for j in range(65, 65+i):
   print(chr(j), end=" ")
 print()


for i in range(5, 0, -1):
 print("*" * i) 
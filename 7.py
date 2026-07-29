#Conditional Statements
i = 1
while i <= 8:
 print(i)
 i += 1
for i in range(8):
 print("Iteration", i)

for i in range(8):
 if i == 2:
  continue
 if i == 4: 
  break
 print(i) 
else:
 pass
#  
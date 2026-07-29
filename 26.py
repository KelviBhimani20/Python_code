#Local and Global Variables Example

x = 20 
def show():
 x = 8 
 print("Local x:", x)
def display():
 global x
 x = x + 8
 print("Modified Global x:", x)
show()
display()
print("Global x after function call:", x)
 
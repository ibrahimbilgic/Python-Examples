#stack -> store items 
# push() -> adds an item.
# pop() -> removes an item.
# LIFO 

while True:
    input_string = input(">> ")
    
    stack = [] 
    
    for char in input_string:
        stack.append(char)
    
    output_string = ""
    
    while len(stack) > 0:
        output_string += stack.pop()
    
    print(output_string)
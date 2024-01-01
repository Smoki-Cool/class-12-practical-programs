# Write a program to implement stack in python using list.

def is_empty(stack: list) -> bool:
    '''
    Checks if the stack is empty.
    '''
    if len(stack) == 0:
        return True
    else:
        return False

def push(item, stack: list):
    '''
    Pushes an element to the top of stack.
    '''
    global top
    
    stack.append(item)
    print("Pushed an element.")
    top += 1

def pop(stack: list):
    '''
    Pops an element from the top of stack and returns it.
    '''
    global top
    
    if is_empty(stack):
        return "Underflow Error."
    else:
        item = stack.pop()
        print("Popped an element.")
        top -= 1
    
    return item

def peek(stack: list):
    '''
    Returns the top element of stack without popping.
    '''
    if is_empty(stack):
        return "Underflow."
    return stack[top]

def display(stack: list):
    '''
    Displays the entire stack.
    '''
    if is_empty(stack):
        print("Stack is empty.")
    else:
        print("Elements:")
        for a in range(top, -1,  -1 ):
            if a == top:
                print(stack[top], "<-- top" )
            else:
                print(stack[a])

stack = []
top = -1

push(19, stack)
push(100, stack)
push(0, stack)
print("Popped element:", pop(stack))
print("Peeking stack:", peek(stack))
display(stack)

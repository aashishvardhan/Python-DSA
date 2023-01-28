# We can implement stacks using Lists in python

stack = [1, 2, 3, 4, 5]
print(stack)

# We use append function in place of push()
stack.append(6)
print(stack)

# We have pop function directly to remove the top element of the stack
stack.pop()
print(stack)

# Instead of peek() we can use stack[-1] to return the value on the top of the stack
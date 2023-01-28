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


# The functions associated with stack are:

# empty() – Returns whether the stack is empty – Time Complexity: O(1)
# size() – Returns the size of the stack – Time Complexity: O(1)
# top() – Returns a reference to the topmost element of the stack – Time Complexity: O(1)
# push(a) – Inserts the element ‘a’ at the top of the stack – Time Complexity: O(1)
# pop() – Deletes the topmost element of the stack – Time Complexity: O(1)
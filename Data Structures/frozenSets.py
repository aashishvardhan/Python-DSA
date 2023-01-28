# Similar to sets, frozen sets also possess the same properties except they are immutable.
var = frozenset([1, 2, 3, 2, 3, 4, 4 ,4, 5, 5])
print(var)

var.add(6)
print(var)

# So, the frozen sets doesn't allow the add operation
x = 1
def test():
    x = 2
test()
print(x)


x = 1
def test():
    global x
    x = 2
test()
print(x)


x = [1]
def test():
    x = [2]
test()
print(x)


x = [1]
def test():
    global x
    x = [2]
test()
print(x)


x = ["game"]
print(x)
print(id(x))
def test():
    x[0] = "a game"
test()
print(x)
print(id(x))

# ===== IMPORTANT NOTES =====
# 
# The key difference between the third and last examples:
# 
# THIRD EXAMPLE (doesn't work):
# x = [2]  - This REBINDS the variable x to a new list
#           - Creates a new list object in memory
#           - The local variable x now points to this new list
#           - The global variable x is untouched
#           - Need 'global x' to modify the global variable
#
# LAST EXAMPLE (works without global):
# x[0] = 2  - This MODIFIES the existing list object
#            - No new object is created
#            - The same list object is changed in place
#            - Since lists are mutable, this works without 'global'
#            - Python finds x in global scope and modifies the list it points to
#
# Think of it like this:
# - x = [2] = "Give me a new list and call it x" (rebinding)
# - x[0] = 2 = "Take the list that x points to and change its first element" (modifying)
#
# That's why the ID stays the same in the last example - same object, modified contents!

# ===== STEP-BY-STEP PROCESS FOR x[0] = 2 =====
#
# When Python encounters x[0] = 2 inside the function:
# 
# STEP 1: Python looks for 'x' in the LOCAL scope (inside the function)
#         - Does 'x' exist as a local variable? NO
# 
# STEP 2: Python looks for 'x' in the GLOBAL scope (outside the function)
#         - Does 'x' exist as a global variable? YES (x = [1])
# 
# STEP 3: Python uses the global 'x' and modifies the list it points to
#         - Changes x[0] from 1 to 2
#         - The list object itself is modified in place
#         - No new object is created
#
# STEP 4: Since we're modifying an existing object (not creating a new one),
#         no 'global' declaration is needed
#
# This is different from x = [2] which would create a NEW local variable!
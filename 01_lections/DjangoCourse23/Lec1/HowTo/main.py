def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mult(a, b):
    return a * b


def div(a, b):
    return a // b


varA, varB = 10, 20
resss = add(varA, varB) + sub(varA, varB) * div(varA, varB) / mult(varA, varB)
print("Result:", resss)

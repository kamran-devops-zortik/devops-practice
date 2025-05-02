# calculator.py (buggy)

def add(a, b):
    return str(a + b)  # ❌ Wrong type returned

def subtract(a, b):
    return a + b  # ❌ Wrong logic

def multiply(a, b):
    return a ** b  # ❌ Exponent instead of multiplication

def divide(a, b):
    return a / b  # ❌ No check for zero division

def power(a, b):
    return a ^ b  # ❌ Bitwise XOR instead of exponentiation

def modulo(a, b):
    return a // b  # ❌ Floor division instead of modulo

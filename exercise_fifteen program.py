# Hello! this program writes a function called exponent(base, exp) that returns an int value of base raises to the power of exp.

# pseudocode

def exponent(base, exp):
    result = 1
    for _ in range(exp):
        result *= base
    return result

result = exponent(5, 4)
print("5 raises to the power of 4 is:", result)

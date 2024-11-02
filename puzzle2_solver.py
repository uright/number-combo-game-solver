import itertools
import multiprocessing

# Define the digits and the target range
digits = ['1', '4', '9', '2']
target_range = range(1, 101)

# Define the operations
operations = ['+', '-', '*', '/', '**']
#operations = ['+', '-', '*', '/']

factorial = lambda n: 1 if n == 0 else n * factorial(n-1)

# Function to evaluate expressions
def evaluate_expression(expr):
    try:
        # Return false if expr consists of '** factorial('
        if '** factorial(' in expr: return False
        if '** (factorial(' in expr: return False
        
        print (expr)
        return eval(expr)
    except (ZeroDivisionError, Exception):  # Catch ZeroDivisionError and all other exceptions
        return None

# Function to generate all possible expressions
def generate_expressions(digits, operations):
    digitsCount = len(digits)
    perm = digits
    
    for ops in itertools.product(operations, repeat=digitsCount-1):
        if (digitsCount == 4):
            yield f"{perm[0]} {ops[0]} {perm[1]} {ops[1]} {perm[2]} {ops[2]} {perm[3]}"
            yield f"{perm[0]} {ops[0]} ( {perm[1]} {ops[1]} {perm[2]} ) {ops[2]} {perm[3]}"
            yield f"{perm[0]} {ops[0]} (( {perm[1]} {ops[1]} {perm[2]} ) {ops[2]} {perm[3]})"
            yield f"{perm[0]} {ops[0]} {perm[1]} {ops[1]} ( {perm[2]} {ops[2]} {perm[3]} )"
            yield f"{perm[0]} {ops[0]} ( {perm[1]} {ops[1]} ( {perm[2]} {ops[2]} {perm[3]} ))"
        elif (digitsCount == 3):
            yield f"{perm[0]} {ops[0]} {perm[1]} {ops[1]} {perm[2]}"
            yield f"{perm[0]} {ops[0]} ({perm[1]} {ops[1]} {perm[2]})"
        elif (digitsCount == 2):
            yield f"{perm[0]} {ops[0]} {perm[1]}"
        else:
            yield perm[0]
    
    # Handle permutation for sticky numbers
    if (digitsCount == 4):
        # if both digits[0] and digits[1] is number
        if (digits[0].isnumeric() and digits[1].isnumeric()):
            numbersStr = f"{digits[0]}{digits[1]},{digits[2]},{digits[3]}"
            for expression in generate_expressions(numbersStr.split(","), operations):
                yield expression
        if (digits[1].isnumeric() and digits[2].isnumeric()):
            numbersStr = f"{digits[0]},{digits[1]}{digits[2]},{digits[3]}"
            for expression in generate_expressions(numbersStr.split(","), operations):
                yield expression
        if (digits[2].isnumeric() and digits[3].isnumeric()):
            numbersStr = f"{digits[0]},{digits[1]},{digits[2]}{digits[3]}"
            for expression in generate_expressions(numbersStr.split(","), operations):
                yield expression
    elif (digitsCount == 3):
        if (digits[0].isnumeric() and digits[1].isnumeric()):
            numbersStr = f"{digits[0]}{digits[1]},{digits[2]}"
            for expression in generate_expressions(numbersStr.split(","), operations):
                yield expression
        if (digits[1].isnumeric() and digits[2].isnumeric()):
            numbersStr = f"{digits[0]},{digits[1]}{digits[2]}"
            for expression in generate_expressions(numbersStr.split(","), operations):
                yield expression
    elif (digitsCount == 2):
        if (digits[0].isnumeric() and digits[1].isnumeric()):
            numbersStr = f"{digits[0]}{digits[1]}"
            for expression in generate_expressions(numbersStr.split(","), operations):
                yield expression

    # Handle permutation for factorial
    factorialComboCount = 2 ** digitsCount
    
    # Loop through each combo of factorialComboCount (skip index 0 as it's already handled)
    for i in range(1, factorialComboCount):
        
        # Create the binary representation of the current number
        binary_repr = bin(i)[2:].zfill(digitsCount)
        
        # Create a copy of the digits to manipulate
        factorial_permuted_digits = perm[:]
        
        # Wrap digits with factorial based on binary representation
        for j in range(digitsCount):
            if binary_repr[j] == '1':
                factorial_permuted_digits[j] = f"factorial({factorial_permuted_digits[j]})"

        # Generate expressions with factorial
        if (digitsCount == 4):
            numbersStr = f"{factorial_permuted_digits[0]}{factorial_permuted_digits[1]},{factorial_permuted_digits[2]},{factorial_permuted_digits[3]}"
            for expression in generate_expressions(numbersStr.split(","), operations):
                yield expression
            numbersStr = f"{factorial_permuted_digits[0]},{factorial_permuted_digits[1]}{factorial_permuted_digits[2]},{factorial_permuted_digits[3]}"
            for expression in generate_expressions(numbersStr.split(","), operations):
                yield expression
            numbersStr = f"{factorial_permuted_digits[0]},{factorial_permuted_digits[1]},{factorial_permuted_digits[2]}{factorial_permuted_digits[3]}"
            for expression in generate_expressions(numbersStr.split(","), operations):
                yield expression
        elif (digitsCount == 3):
            numbersStr = f"{factorial_permuted_digits[0]}{factorial_permuted_digits[1]},{factorial_permuted_digits[2]}"
            for expression in generate_expressions(numbersStr.split(","), operations):
                yield expression
            numbersStr = f"{factorial_permuted_digits[0]},{factorial_permuted_digits[1]}{factorial_permuted_digits[2]}"
            for expression in generate_expressions(numbersStr.split(","), operations):
                yield expression
        elif (digitsCount == 2):
            numbersStr = f"{factorial_permuted_digits[0]}{factorial_permuted_digits[1]}"
            for expression in generate_expressions(numbersStr.split(","), operations):
                yield expression
            
# Main function to find valid expressions
def find_valid_expressions():
    valid_expressions = {}
    for expr in generate_expressions(digits, operations):
        result = evaluate_expression(expr)
        if result in target_range and result not in valid_expressions:
            valid_expressions[result] = expr
    return valid_expressions

# Run the solver
if __name__ == "__main__":
    valid_expressions = find_valid_expressions()
    for result, expr in sorted(valid_expressions.items()):
        print(f'"{expr.replace('factorial(4)','4!')}",{result}')

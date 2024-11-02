import itertools
import operator
import math

# Define the digits and the target range
digits = ['1', '9', '4', '2']
target_range = range(1, 101)

# Define the operations
operations = ['+', '-', '*', '/', '**', 'factorial']

# Function to evaluate expressions
def evaluate_expression(expr):
    try:
        return eval(expr)
    except ZeroDivisionError:
        return None

# Function to generate all possible expressions
def generate_expressions(digits, operations):
    for ops in itertools.product(operations, repeat=len(digits)-1):
        for perm in itertools.permutations(digits):
            # Create expression by interleaving digits and operations
            expr = ''.join(f"{perm[i]}{ops[i]}" for i in range(len(ops))) + perm[-1]
            yield expr

# Main function to find valid expressions
def find_valid_expressions():
    valid_expressions = []
    for expr in generate_expressions(digits, operations):
        result = evaluate_expression(expr)
        if result in target_range:
            valid_expressions.append((expr, result))
    return valid_expressions

# Run the solver
if __name__ == "__main__":
    valid_expressions = find_valid_expressions()
    for expr, result in valid_expressions:
        print(f"{expr} = {result}")

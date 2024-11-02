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
    # Generate expressions with parentheses
    n = len(digits)
    for ops in itertools.product(operations, repeat=n-1):
        for perm in itertools.permutations(digits):
            # Create expressions without parentheses
            expr = ''.join(f"{perm[i]}{ops[i]}" for i in range(len(ops))) + perm[-1]
            yield expr
            
            # Create expressions with parentheses
            for i in range(n):
                for j in range(i + 1, n + 1):
                    if j - i > 1:  # Ensure at least two digits are grouped
                        grouped = ''.join(f"{perm[k]}{ops[k]}" for k in range(i)) + \
                                  f"({''.join(perm[i:j])})" + \
                                  ''.join(f"{perm[k]}{ops[k-1]}" for k in range(j, n))
                        if grouped[-1] not in operations:  # Ensure no trailing operator
                            yield grouped
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

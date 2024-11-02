import itertools
import multiprocessing

# Define the digits and the target range
digits = ['1', '9', '4', '2']
target_range = range(1, 101)

# Define the operations
operations = ['+', '-', '*', '/']
#operations = ['+', '-', '*', '/', '**']

factorial = lambda n: 1 if n == 0 else n * factorial(n-1)

# Function to evaluate expressions
def evaluate_expression(expr):
    try:
        return eval(expr)
    except (ZeroDivisionError, Exception):  # Catch ZeroDivisionError and all other exceptions
        return None

# Function to generate all possible expressions
def generate_expressions(digits, operations):
    # Generate expressions with parentheses
    n = len(digits)
    for perm in itertools.permutations(digits):
        for ops in itertools.product(operations, repeat=n-1):
            yield f"{perm[0]} {ops[0]} {perm[1]} {ops[1]} {perm[2]} {ops[2]} {perm[3]}"
            yield f"{perm[0]} {ops[0]} ( {perm[1]} {ops[1]} {perm[2]} ) {ops[2]} {perm[3]}"
            yield f"{perm[0]} {ops[0]} (( {perm[1]} {ops[1]} {perm[2]} ) {ops[2]} {perm[3]})"
            yield f"{perm[0]} {ops[0]} {perm[1]} {ops[1]} ( {perm[2]} {ops[2]} {perm[3]} )"
            yield f"{perm[0]} {ops[0]} ( {perm[1]} {ops[1]} ( {perm[2]} {ops[2]} {perm[3]} ))"
            
            yield f"{perm[0]}{perm[1]} {ops[1]} {perm[2]} {ops[2]} {perm[3]}"
            yield f"{perm[0]}{perm[1]} {ops[1]} ( {perm[2]} {ops[2]} {perm[3]} )"
            
            # Comment out when using '**' operator
            yield f"{perm[0]} {ops[0]} {perm[1]} {ops[1]} {perm[2]} {ops[2]} {perm[3]}".replace('4', 'factorial(4)')
            yield f"{perm[0]} {ops[0]} ( {perm[1]} {ops[1]} {perm[2]} ) {ops[2]} {perm[3]}".replace('4', 'factorial(4)')
            yield f"{perm[0]} {ops[0]} (( {perm[1]} {ops[1]} {perm[2]} ) {ops[2]} {perm[3]})".replace('4', 'factorial(4)')
            yield f"{perm[0]} {ops[0]} {perm[1]} {ops[1]} ( {perm[2]} {ops[2]} {perm[3]} )".replace('4', 'factorial(4)')
            yield f"{perm[0]} {ops[0]} ( {perm[1]} {ops[1]} ( {perm[2]} {ops[2]} {perm[3]} ))".replace('4', 'factorial(4)')
            
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

import itertools
import re

def extract_variables(*expressions):
    """Extract unique variable names matching single capital letters (A-Z) from the inputs."""
    variables = set()
    for expr in expressions:
        variables.update(re.findall(r'\b[A-Z]\b', expr))
    return sorted(list(variables))

def evaluate_expression(expr, assignment):
    """Evaluate boolean expression string by substituting variables with their assigned values."""
    clean_expr = expr.replace("and", "and").replace("or", "or").replace("not", "not ")
    return int(eval(clean_expr, {}, assignment))

kb_input = "(not A or B) and (not B or C) and A"
alpha_input = "C"

variables = extract_variables(kb_input, alpha_input)
header = " | ".join(variables) + " || KB | Alpha"
print(header)
print("-" * len(header))

entails = True
combinations = list(itertools.product([0, 1], repeat=len(variables)))

for combo in combinations:
    assignment = dict(zip(variables, combo))

    kb_val = evaluate_expression(kb_input, assignment)
    alpha_val = evaluate_expression(alpha_input, assignment)

    row_str = " | ".join(str(assignment[v]) for v in variables)
    print(f"{row_str} ||  {kb_val}  |   {alpha_val}")

    if kb_val == 1 and alpha_val == 0:
        entails = False

print("-" * len(header))
if entails:
    print("\nResult: KB entails Alpha (KB |= Alpha) is TRUE. (Therefore, C is proved!)")
else:
    print("\nResult: KB entails Alpha (KB |= Alpha) is FALSE.")
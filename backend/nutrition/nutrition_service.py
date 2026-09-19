from sympy import symbols, solve

x = symbols('x')

equation = x - 25

result = solve(equation)

print("Required fodder:", result[0], "kg")
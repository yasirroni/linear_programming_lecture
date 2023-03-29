import cvxpy as cp

# Define the decision variables
x = cp.Variable(integer=True)  # x >= 0
y = cp.Variable(integer=True)  # y >= 0

# Define the objective function
objective = cp.Maximize(20*x + 25*y)

# Define the constraints
constraints = [
    2*x + 3*y <= 30,
    3*x + 1*y <= 20,
]

# Define and solve the problem
problem = cp.Problem(objective, constraints)
problem.solve()

# Print the optimal solution and optimal value
print("Optimal solution: x =", x.value, ", y =", y.value)
print("Optimal value:", problem.value)

# Check solution
import numpy as np

# Define the decision variables
x = x.value
y = y.value

# Define the constraints
A = [
    lambda x, y: 2*x + 3*y,
    lambda x, y: 3*x + 1*y,
]

rhs = [
    30,
    20,
]

for A_, rhs_ in zip(A, rhs):
    if A_(x, y) > rhs_:
        print(f"Constraint {A_.__name__} is violated with value {A_(x, y)} > {rhs_}.")
    else:
        print(f"Constraint {A_.__name__} is satisfied with value {A_(x, y)} <= {rhs_}.")
